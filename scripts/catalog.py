"""Validate community metadata, verify opt-in badges and build the static directory."""
from __future__ import annotations
import argparse
import base64
import json
import re
import shutil
from datetime import datetime, timedelta, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse, quote
from urllib.request import Request, urlopen
import os

ROOT = Path(__file__).resolve().parents[1]
from site_config import SITE, TOOL_TYPES, LEGACY_SITES
CATEGORIES = ['Creative', '3D & Blender', 'Coding', 'Research', 'Data', 'Operations', 'Other']
REPO = re.compile(r'https://github\.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+)\Z')
SLUG = re.compile(r'[a-z0-9]+(?:-[a-z0-9]+)*\Z')
UTC = timezone.utc

def load(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))

def save(path, value):
    path = Path(path)
    temporary = path.with_suffix('.tmp')
    temporary.write_text(json.dumps(value, indent=2) + '\n', encoding='utf-8')
    temporary.replace(path)

def https(value):
    if not isinstance(value, str):
        raise ValueError('URL must be text')
    p = urlparse(value)
    if p.scheme != 'https' or not p.hostname or p.username or p.password or any(c.isspace() for c in value):
        raise ValueError('Use a public HTTPS URL without credentials')
    return value

def text(value, field):
    if not isinstance(value, str) or not value.strip() or len(value) > 5000:
        raise ValueError(f'{field} needs nonempty text (max 5000 characters)')

def validate_entry(e):
    allowed = {'schema_version','id','name','summary','category','repository','license','version','distribution','installation','manual_setup','notes','contents','harneloop','documentation','type','image'}
    if not isinstance(e, dict) or set(e) - allowed:
        raise ValueError('Unknown listing fields; review/boost labels are maintainer-owned')
    if e.get('schema_version') != 1 or not SLUG.fullmatch(e.get('id','')):
        raise ValueError('Use schema_version 1 and a lowercase slug')
    for field in ['name','summary','license','version']:
        text(e.get(field), field)
    if e.get('category') not in CATEGORIES:
        raise ValueError('Unknown category')
    https(e.get('repository'))
    if e.get('type', 'Harness') not in TOOL_TYPES:
        raise ValueError('Unknown tool type')
    if 'image' in e:
        image = e['image']
        if not isinstance(image, dict) or set(image) != {'url','alt','source'}:
            raise ValueError('Optional image needs url, alt and source')
        text(image['alt'], 'image alt text')
        https(image['source'])
        url = image['url']
        if isinstance(url, str) and url.startswith('assets/logos/'):
            if not re.fullmatch(r'assets/logos/[a-z0-9][a-z0-9.-]*\.(?:png|webp|jpg|svg)', url):
                raise ValueError('Invalid local logo path')
        else:
            https(url)
    d = e.get('distribution', {})
    if set(d) - {'kind','url','label','scope','repository_has_extra_material','branch'}:
        raise ValueError('Unknown distribution fields')
    if d.get('kind') not in {'package','dedicated-branch','focused-repository','service','api'}:
        raise ValueError('Declare a package, dedicated branch, focused repository, service or API')
    if not isinstance(d.get('repository_has_extra_material'), bool):
        raise ValueError('Declare whether the repository has extra material')
    if d['repository_has_extra_material'] and d['kind'] == 'focused-repository':
        raise ValueError('Mixed repositories require a package or dedicated branch')
    https(d.get('url'))
    text(d.get('label'), 'distribution label')
    text(d.get('scope'), 'distribution scope')
    if d['kind'] == 'dedicated-branch':
        text(d.get('branch'), 'dedicated branch')
        if d['url'] != e['repository'] + '/tree/' + quote(d['branch'], safe='/'):
            raise ValueError('Dedicated branch URL must match the declared source branch')
    if not isinstance(e.get('installation'), list) or not e['installation']:
        raise ValueError('Clear installation instructions are required')
    for step in e['installation']:
        if not isinstance(step, dict) or set(step) - {'title','body','command','url','label'}:
            raise ValueError('Invalid install step')
        text(step.get('title'), 'step title')
        text(step.get('body'), 'step body')
        if 'command' in step:
            text(step['command'], 'install command')
        if 'url' in step:
            https(step['url'])
            text(step.get('label'), 'step link label')
    for field in ['manual_setup','notes']:
        if not isinstance(e.get(field), list):
            raise ValueError(f'{field} must be a list (use [] for none)')
        for value in e[field]:
            text(value, field)
    if 'documentation' in e:
        https(e['documentation'])
    if 'contents' in e:
        c = e['contents']
        if not isinstance(c, dict) or set(c) - {'skills','references','renderers','files','mcp_tools','tools'}:
            raise ValueError('Invalid optional component counts')
        for key, value in c.items():
            if key == 'tools':
                if not isinstance(value, list):
                    raise ValueError('tools must be a list')
                for item in value: text(item, 'tool')
            elif not isinstance(value, int) or isinstance(value, bool) or value < 0:
                raise ValueError('Component counts must be nonnegative integers')
    if 'harneloop' in e:
        if not isinstance(e['harneloop'], dict) or set(e['harneloop']) != {'url','detail'}:
            raise ValueError('Harneloop attribution needs url and detail')
        https(e['harneloop']['url'])
        text(e['harneloop']['detail'], 'Harneloop attribution')
    return e

def entries(root=ROOT):
    out=[]
    for file in sorted((root / 'data/listings').glob('*.json')):
        e=validate_entry(load(file))
        if file.stem != e['id']:
            raise ValueError('Filename must match listing id')
        out.append(e)
    if len({e['id'] for e in out}) != len(out):
        raise ValueError('Duplicate ids')
    return out

def parse_time(value):
    date=datetime.fromisoformat(value.replace('Z','+00:00'))
    if date.tzinfo is None: raise ValueError('Boost timestamps require a timezone')
    return date.astimezone(UTC)

def iso(date):
    return date.astimezone(UTC).isoformat(timespec='seconds').replace('+00:00','Z')

def active(grant, now):
    if not grant or grant.get('badge_present') is not True: return False
    start,end,checked=(parse_time(grant[k]) for k in ['granted_at','expires_at','last_checked_at'])
    if end-start != timedelta(days=14): raise ValueError('Boost must last exactly 14 days')
    return start <= now < end and timedelta(0) <= now-checked <= timedelta(hours=48)

def validate_grants(grants):
    for grant in grants.values():
        if set(grant) != {'granted_at','expires_at','last_checked_at','badge_present','readme_url'}:
            raise ValueError('Invalid boost receipt')
        start,end,checked=(parse_time(grant[k]) for k in ['granted_at','expires_at','last_checked_at'])
        if end-start != timedelta(days=14) or checked < start:
            raise ValueError('Invalid 14-day boost timestamps')
        if not isinstance(grant['badge_present'],bool): raise ValueError('Badge presence must be boolean')
        https(grant['readme_url'])

class BadgeHTML(HTMLParser):
    def __init__(self, target, badge):
        super().__init__();self.target=target;self.badge=badge;self.link=False;self.found=False
    def handle_starttag(self, tag, attrs):
        attrs=dict(attrs)
        if tag=='a': self.link=attrs.get('href')==self.target
        if tag=='img' and self.link and attrs.get('src')==self.badge and attrs.get('alt','').lower() in {'listed in toolindex','listed in harness library'}: self.found=True
    def handle_endtag(self, tag):
        if tag=='a': self.link=False

def has_badge(readme, slug):
    # Read only first 30 lines, ignore comments/fenced examples. Never execute content.
    head='\n'.join(readme.splitlines()[:30])
    head=re.sub(r'<!--.*?(?:-->|$)','',head,flags=re.S)
    clean=[];fenced=False
    for line in head.splitlines():
        if line.lstrip().startswith(('```','~~~')): fenced=not fenced;continue
        if not fenced and not line.startswith(('    ','\t')): clean.append(line)
    head='\n'.join(clean)
    head=re.sub(r'`+[^`]*`+','',head)
    # Preserve existing grants across the organization migration. New badges use SITE.
    sites=[SITE,*LEGACY_SITES]
    pairs=[(site+'badges/'+slug+'.svg',target) for site in sites
           for target in [site+'#'+slug,site+'tools/'+slug+'/',site+'harnesses/'+slug+'/']]
    for badge,target in pairs:
        if any('[!['+name+']('+badge+')]('+target+')' in head for name in ['Listed in ToolIndex','Listed in Harness Library']): return True
        parser=BadgeHTML(target,badge);parser.feed(head)
        if parser.found: return True
    return False

def readme(e):
    match=REPO.fullmatch(e['repository'])
    if not match:
        raise ValueError('Automatic badge verification currently supports GitHub sources only')
    url=f'https://api.github.com/repos/{match[1]}/{match[2]}/readme'
    headers={'Accept':'application/vnd.github+json','User-Agent':'ToolIndex-badge-check'}
    if os.environ.get('GITHUB_TOKEN'): headers['Authorization']='Bearer '+os.environ['GITHUB_TOKEN']
    with urlopen(Request(url,headers=headers),timeout=20) as response:
        data=response.read(1_000_001)
    if len(data)>1_000_000: raise ValueError('README response too large')
    payload=json.loads(data)
    if payload.get('encoding')!='base64': raise ValueError('Unsupported README encoding')
    return base64.b64decode(payload['content']).decode('utf-8'),payload['html_url']

def refresh(listings, receipt, now, fetch=readme):
    grants=receipt.setdefault('grants',{})
    for e in listings:
        try: content,url=fetch(e)
        except Exception as error:
            print(f"Badge check unavailable for {e['id']}: {type(error).__name__}");continue
        present=has_badge(content,e['id']);grant=grants.get(e['id'])
        if present and not grant:
            grant={'granted_at':iso(now),'expires_at':iso(now+timedelta(days=14))};grants[e['id']]=grant
        if grant:
            grant.update(badge_present=present,last_checked_at=iso(now),readme_url=url)
        print(f"{e['id']}: badge {'present' if present else 'absent'}")
    return receipt

def checked_catalog(root=ROOT, now=None):
    now=now or datetime.now(UTC);listing=entries(root);reviews=load(root/'data/reviews.json')['reviews'];grants=load(root/'data/boosts.json')['grants']
    validate_grants(grants)
    ids={e['id'] for e in listing}
    if set(reviews)-ids or set(grants)-ids: raise ValueError('Review/boost references an unknown listing')
    for slug,r in reviews.items():
        if r.get('status') not in {'setup-reviewed','artifact-checked'}: raise ValueError('Unknown review status')
        text(r.get('evidence'),'review evidence');https(r.get('url'))
        datetime.strptime(r['reviewed_at'],'%Y-%m-%d')
        if not isinstance(r.get('built_with_harneloop'),bool): raise ValueError('Attribution review must be boolean')
    result=[]
    for e in listing:
        review=reviews.get(e['id'])
        if not review: continue # Only approved listings are published.
        if review['built_with_harneloop'] and 'harneloop' not in e: raise ValueError('Approved attribution needs a source')
        boost=grants.get(e['id']);is_active=active(boost,now)
        if e.get('image',{}).get('url','').startswith('assets/logos/') and not (root/'site'/e['image']['url']).is_file():
            raise ValueError('Declared local logo is missing')
        result.append({**e,'type':e.get('type','Harness'),'url':SITE+'tools/'+e['id']+'/','review':review,'boost':boost if is_active else None})
    result.sort(key=lambda e:(not bool(e['boost']),e['name'].casefold()))
    return {'generated_at':iso(now),'categories':CATEGORIES,'listings':result}

def badge(slug):
    return '<svg xmlns="http://www.w3.org/2000/svg" width="218" height="28" role="img" aria-label="Listed in ToolIndex"><title>Listed in ToolIndex</title><rect width="218" height="28" rx="5" fill="#252727"/><g transform="translate(7,2) scale(.52)" fill="none" stroke="#ff8243" stroke-width="4.5"><circle cx="17" cy="29" r="12.5"/><circle cx="34" cy="17" r="12.5"/></g><text x="43" y="18" fill="#fff" font-family="Arial,sans-serif" font-size="11">Listed in ToolIndex</text></svg>'

def build(root=ROOT):
    catalog=checked_catalog(root);destination=root/'dist';destination.mkdir(exist_ok=True)
    for source in (root/'site').rglob('*'):
        if source.is_file() and source != root/'site/layout.html':
            target=destination/source.relative_to(root/'site');target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(source,target)
    save(destination/'catalog.json',catalog)
    (destination/'badges').mkdir(exist_ok=True)
    for e in catalog['listings']:(destination/'badges'/f"{e['id']}.svg").write_text(badge(e['id']),encoding='utf-8')
    from publishing import publish
    publish(root,destination,catalog)
    (destination/'.nojekyll').touch()
    print(f"Built {len(catalog['listings'])} reviewed listings")

def main():
    parser=argparse.ArgumentParser();parser.add_argument('command',choices=['validate','build','refresh']);args=parser.parse_args()
    if args.command=='refresh':
        receipt=load(ROOT/'data/boosts.json');save(ROOT/'data/boosts.json',refresh(entries(),receipt,datetime.now(UTC)))
    elif args.command=='build': build()
    else: checked_catalog();print('Catalog valid')

if __name__=='__main__': main()
