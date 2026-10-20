"""Public static pages and text resources. Submitted strings are escaped, never executed."""
from __future__ import annotations
from html import escape
import json
import re
from pathlib import Path
from xml.etree import ElementTree as ET

SITE = 'https://openrootdev.github.io/harness-library/'
BASE = '/harness-library/'
REPOSITORY = 'https://github.com/OpenRootdev/harness-library'
FORM = REPOSITORY + '/issues/new?template=submit-harness.yml'
DEFINITION = ('An agent harness is the surrounding setup that lets an AI model act on a task. '
              'It can include instructions, skills, tools, environment mappings, checks and workflows. '
              'Harness Library focuses on reusable, task-specific setups: from a small skill folder '
              'to an MCP workflow or a larger harness package.')
WELCOME = 'New submissions are welcome. We’re looking for practical harnesses people can actually install and use.'
SUBMIT_STEPS = [
    ('Share your repository', 'Open the short GitHub form with a name, repository link and the task your harness helps an agent do. No fork or pull request is needed.'),
    ('Explain how to install it', 'Add the focused package or harness branch, version and license, then list the install steps and anything people must connect or configure manually.'),
    ('Get reviewed and listed', 'Maintainers check the setup and distribution scope, ask questions in your issue if needed, and publish approved listings. You can update the listing later.')
]
FAQ = [
    ('Can I submit just a few skills?', 'Yes. A useful skill folder, MCP workflow or complete harness package can qualify. Explain the task, installation and manual setup clearly.'),
    ('Do I need to use Harneloop?', 'No. Submissions can use any agent or framework. Built with Harneloop is an optional attribution, reviewed separately from the listing.'),
    ('What if my repository contains a whole application?', 'Provide a focused package or a dedicated harness branch so users can install only the harness. Do not make them download unrelated videos, caches or application assets.'),
    ('Does a listing mean it works with every model?', 'No. Each page states its review scope, evidence and manual prerequisites. Setup reviewed and artifacts checked are different claims; neither guarantees every platform or model.'),
    ('Is submitting free?', 'Yes. Browsing and submitting to the directory are free. You need a GitHub account to open a submission issue; a Harness Library account is not required.')
]

def h(value):
    return escape(str(value), quote=True)

def local(path=''):
    return BASE + path

def harness_path(e):
    return 'harnesses/' + e['id'] + '/'

def boost_attributes(e):
    boost = e.get('boost') or {}
    return ' '.join(f'data-{key}="{h(boost.get(field,""))}"' for key,field in [('boost-start','granted_at'),('boost-end','expires_at'),('boost-checked','last_checked_at')])

def json_script(value):
    return json.dumps(value, ensure_ascii=False, separators=(',', ':')).replace('<', '\\u003c')

def a(text, url, cls=''):
    return f'<a href="{h(url)}"' + (f' class="{h(cls)}"' if cls else '') + f'>{h(text)}</a>'

def codebox(value, identifier, label='Copy code or path'):
    return (f'<div class="codebox"><pre id="{h(identifier)}"><code>{h(value)}</code></pre>'
            f'<button type="button" class="copy" data-copy-target="{h(identifier)}" aria-label="{h(label)}" hidden>Copy</button></div>')

def labels(e):
    parts = [f'<span class="label category">{h(e["category"])}</span>']
    if e['review']['built_with_harneloop']:
        parts.append(a('Built with Harneloop', e['harneloop']['url'], 'label'))
    kind = {'package':'Packaged','dedicated-branch':'Harness branch','focused-repository':'Focused repository'}[e['distribution']['kind']]
    parts.append(f'<span class="label">{kind}</span>')
    if e.get('boost'):
        parts.append(f'<span class="label boost" data-boost-for="{h(e["id"])}" title="Free initial 14-day badge boost">Community boost</span>')
    return '<div class="labels">' + ''.join(parts) + '</div>'

def list_section(title, values, cls='', level=3):
    items = ''.join(f'<li>{h(v)}</li>' for v in values)
    body = '<ul>' + items + '</ul>' if items else '<p>None declared.</p>'
    return f'<section class="{h(cls)}"><h{level}>{h(title)}</h{level}>{body}</section>'

def icon(name):
    return f'<svg class="icon" viewBox="0 0 256 256" aria-hidden="true"><use href="{local("assets/icons.svg")}#{name}"></use></svg>'

def listing(e):
    art = 'blender.svg' if e['id'] == 'vipermesh-blender' else 'motion.svg'
    search = ' '.join([e['name'], e['summary'], e['category'], *e['notes'], *e.get('contents',{}).get('tools',[])])
    package = 'MCP bundle + addon' if e['id'] == 'vipermesh-blender' else 'Skill package' if e.get('contents',{}).get('skills') else 'Harness package'
    return (f'<article id="{h(e["id"])}" class="listing" data-harness-id="{h(e["id"])}" data-category="{h(e["category"])}" data-search="{h(search)}" {boost_attributes(e)}>'
            f'<div class="thumb"><img src="{local("assets/"+art)}" alt="" width="80" height="80"></div>'
            '<div class="listing-body"><h2>' + a(e['name'],local(harness_path(e))) + '</h2>'
            f'<p>{h(e["summary"])}</p>{labels(e)}</div><div class="listing-action">'
            + f'<a href="{local(harness_path(e))}">View harness {icon("ArrowRight")}</a>' + f'<span>{icon("Package" if e["id"]=="vipermesh-blender" else "BookOpen")}{package}</span></div></article>')

def faq_html(items=FAQ):
    return '<div class="faq-list">' + ''.join(f'<details><summary>{h(q)}</summary><p>{h(answer)}</p></details>' for q,answer in items) + '</div>'

def invitation():
    return ('<section class="submission-callout" id="submissions" aria-labelledby="welcome-title">'
            '<div><p class="welcome-label">New submissions welcome</p><h2 id="welcome-title">Your harness could be next.</h2>'
            '<p>Built a useful skill folder, MCP workflow or agent harness? We’d love to list it. Share your repository and setup instructions through a short GitHub form.</p>'
            '<p class="submission-note">Free to submit. No fork or pull request needed.</p></div>'
            '<div class="submission-action">' + a('Submit your harness →',local('submit/'),'button')
            + '<span class="welcome-hand" aria-hidden="true">share the good stuff</span></div></section>')

def home(catalog):
    buttons = ''.join(f'<button type="button" aria-pressed="{str(value=="All").lower()}" disabled>{h(value)}</button>'
                      for value in ['All',*dict.fromkeys(e['category'] for e in catalog['listings'])])
    return ('<section id="browse"><div class="hero"><div class="hero-copy">'
            '<h1>Good agents start<br>with a good harness.</h1>'
            '<p>Discover reusable AI agent harnesses: skills, tools, and workflows. Install only what you need.</p></div>'
            f'<div class="hero-sketch" aria-hidden="true"><img src="{local("assets/harness-sketch.svg")}" alt="" width="340" height="270"><span class="sketch-note">find your<br>starting point</span></div></div>'
            f'<div class="controls"><label class="search">{icon("MagnifyingGlass")}'
            '<span class="sr-only">Search harnesses</span><input id="search" type="search" placeholder="Search harnesses…" autocomplete="off" disabled></label>'
            f'<div id="categories" class="categories" role="group" aria-label="Filter by category">{buttons}</div></div>'
            '<noscript><p class="no-js-note">Search needs JavaScript. You can still browse every harness and its installation page below.</p></noscript>'
            f'<p id="count" class="sr-only" role="status" aria-live="polite">{len(catalog["listings"])} harnesses shown</p>'
            '<div id="listings" aria-label="Harness listings">' + ''.join(listing(e) for e in catalog['listings']) + '</div>'
            '<p id="empty" class="empty" hidden>No harnesses match yet. Try another search or category.</p></section>'
            + invitation() + '<section class="library-intro" aria-labelledby="harness-definition"><h2 id="harness-definition">What is an agent harness?</h2>'
            f'<p>{h(DEFINITION)}</p><p>{a("How the library works →",local("about/"))}</p></section>')

def detail(e):
    steps = []
    for i,step in enumerate(e['installation']):
        body = f'<li><h3>{h(step["title"])}</h3><p>{h(step["body"])}</p>'
        if step.get('url'): body += a(step['label']+' ↗',step['url'])
        if step.get('command'): body += codebox(step['command'],f'copy-{e["id"]}-{i}','Copy '+step['title'])
        steps.append(body+'</li>')
    names = {'skills':'skills','references':'references','renderers':'renderers','files':'skill files','mcp_tools':'top-level MCP tools'}
    counts = ''.join(f'<div><strong>{value}</strong><span>{h(names[key].removesuffix("s") if value==1 else names[key])}</span></div>'
                     for key,value in e.get('contents',{}).items() if key!='tools')
    r=e['review']; review_name='Artifacts checked' if r['status']=='artifact-checked' else 'Setup reviewed'
    aside = '<aside class="detail-aside"><h2>Inside this harness</h2><div class="inside">'+counts+'</div>'
    if e.get('contents',{}).get('tools'): aside += list_section('Execution tools',e['contents']['tools'])
    aside += (f'<section class="aside-section"><h3>{review_name}</h3><p>{h(r["evidence"])}</p>'
              + a('Review source ↗',r['url'],'review-link')
              + f'<p class="version-line">Reviewed <time datetime="{h(r["reviewed_at"])}">{h(r["reviewed_at"])}</time></p></section>'
              + f'<section class="aside-section"><h3>License</h3><p>{h(e["license"])}</p>'
              + a('Upstream documentation ↗',e.get('documentation',e['repository']))+'</section>')
    if r['built_with_harneloop']: aside += f'<section class="aside-section"><h3>Built with Harneloop</h3><p>{h(e["harneloop"]["detail"])}</p></section>'
    snippet=f'[![Listed in Harness Library]({SITE}badges/{e["id"]}.svg)]({SITE}{harness_path(e)})'
    aside += ('<section class="badge-offer"><h3>Listed here? Add the badge.</h3>'
              '<p>Place this badge and backlink near the top of your repository README. After verification, get one free 14-day community boost.</p>'
              f'<div class="badge-art"><img src="{local("badges/"+e["id"]+".svg")}" alt="Listed in Harness Library" width="218" height="28">'
              '<span class="badge-note" aria-hidden="true">give yours a boost</span>'
              f'<img class="badge-pointer" src="{local("assets/badge-pointer.svg")}" alt="" aria-hidden="true"></div>'
              + codebox(snippet,'copy-badge-'+e['id'],'Copy listing badge Markdown') + a('How the boost works ↗',REPOSITORY+'/blob/main/docs/badge-program.md'))
    if e.get('boost'): aside += f'<p class="version-line" data-boost-for="{h(e["id"])}">Active until <time datetime="{h(e["boost"]["expires_at"])}">{h(e["boost"]["expires_at"])}</time> (UTC).</p>'
    aside += '</section></aside>'
    return (a('← Back to library',BASE,'back') + f'<section aria-labelledby="harness-title" data-harness-id="{h(e["id"])}" {boost_attributes(e)}><div class="detail-head"><h1 id="harness-title">{h(e["name"])}</h1>'
            f'<p>{h(e["summary"])}</p>{labels(e)}</div><div class="detail-grid"><div><h2>Installation</h2><div class="actions">'
            + a(e['distribution']['label']+' ↓',e['distribution']['url'],'button') + a('Source repository ↗',e['repository'])
            + f'</div><p class="version-line">Version {h(e["version"])} · {h(e["distribution"]["scope"])}</p>'
            + '<ol class="install-steps">'+''.join(steps)+'</ol>'
            + list_section('Manual setup',e['manual_setup'],'manual') + list_section('Additional notes',e['notes'],'notes')
            + '</div>'+aside+'</div></section>')

def submission():
    steps=''.join(f'<li><h2>{h(title)}</h2><p>{h(body)}</p></li>' for title,body in SUBMIT_STEPS)
    return (a('← Back to library',BASE,'back')+'<div class="guide-head"><p class="welcome-label">New submissions welcome</p>'
            '<h1>Share a harness people can use.</h1><p>'+h(WELCOME)+'</p>'
            '<p>A few skills or a complete workflow can be enough. Harneloop is optional.</p><div class="actions">'
            + a('Open the submission form ↗',FORM,'button') + a('Prefer a pull request?',REPOSITORY+'/blob/main/CONTRIBUTING.md')+'</div></div>'
            '<div class="guide-grid"><section aria-label="Submission steps"><ol class="submit-steps">'+steps+'</ol>'
            '<section class="guide-checklist"><h2>What to have ready</h2><ul>'
            '<li>Your repository link, harness name and a short description of the task.</li>'
            '<li>Install steps, version or pinned revision, license and manual setup notes.</li>'
            '<li>A focused package or dedicated harness branch if the repo includes unrelated material.</li>'
            '</ul><p>Skill counts, tool counts, extra notes and test evidence are welcome but optional. Write “none” where no manual setup is needed.</p>'
            '<p>A GitHub account is all you need to submit. Please share setup requirements, not secrets or credentials.</p></section></section>'
            '<aside class="submission-aside"><h2>What we’re looking for</h2><p>Useful, reusable setups for coding, research, data, creative work, Blender and operations. A small clear harness is welcome.</p>'
            '<h3>Clear setup matters</h3><p>We review installation, package scope and any claimed evidence before publishing. We’ll use your submission issue for questions and updates.</p>'
            '<h3>A free listing boost</h3><p>After approval, adding the linked listing badge near the top of your README can earn one transparent 14-day community boost.</p>'
            + a('Read the badge program ↗',REPOSITORY+'/blob/main/docs/badge-program.md')+'</aside></div>'
            '<section class="faq-section"><h2>Before you submit</h2>'+faq_html(FAQ[:3]+FAQ[4:])+'</section>')

def about():
    return (a('← Back to library',BASE,'back')+'<article class="about-content"><h1>An open library for agent harnesses.</h1>'
            '<p class="guide-lead">Find a reusable starting point, understand its setup, and improve it for your task.</p>'
            '<h2>What this directory includes</h2><p>'+h(DEFINITION)+'</p>'
            '<p>Each listing links to its source and focused distribution, explains installation and manual connections, and states the license and review scope. Component counts are optional.</p>'
            '<h2>Harnesses, skills and MCP servers</h2><p>A skill can supply instructions; an MCP server can expose tools. A task-specific harness can combine those pieces with a workflow and checks. The library welcomes both compact skill-based setups and larger packaged workflows, as long as their scope is clear.</p>'
            '<p>For background on the general term, see '+a('Anthropic’s agent evaluation glossary','https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents')+'.</p>'
            '<h2>Review and attribution</h2><p>“Setup reviewed” means the installation and distribution were examined. “Artifacts checked” refers to the specific evidence described on the page. Neither means every model or platform was tested.</p>'
            '<p>Harneloop is optional. “Built with Harneloop” is a separate attribution for harnesses created or improved through '+a('Harneloop','https://harneloop.kaelux.dev/')+'. The directory is not limited to that framework.</p>'
            '<h2>Who maintains it?</h2><p>Maintained by '+a('Kristofer Jussmann (@Ker102)','https://github.com/Ker102')
            + '. Source, changes, submission issues and review records are public in '+a('the Harness Library repository',REPOSITORY)+'.</p>'
            '<p>'+h(WELCOME)+' '+a('See how to submit →',local('submit/'))+'</p>'
            '<h2>Common questions</h2>'+faq_html()+'</article>')

def graph(path, title, description, entries, kind='WebPage', e=None):
    page_url=SITE+path
    website={'@type':'WebSite','@id':SITE+'#website','url':SITE,'name':'Harness Library','description':'An open directory of reusable AI agent harnesses with clear installation instructions.','publisher':{'@id':SITE+'#maintainer'}}
    person={'@type':'Person','@id':SITE+'#maintainer','name':'Kristofer Jussmann','url':'https://github.com/Ker102'}
    page={'@type':kind,'@id':page_url+'#page','url':page_url,'name':title,'description':description,'isPartOf':{'@id':SITE+'#website'},'inLanguage':'en'}
    nodes=[website,person,page]
    if kind=='CollectionPage':
        page['mainEntity']={'@type':'ItemList','itemListElement':[{'@type':'ListItem','position':i+1,'name':row['name'],'url':SITE+harness_path(row)} for i,row in enumerate(entries)]}
    if path:
        crumb={'@type':'BreadcrumbList','@id':page_url+'#breadcrumbs','itemListElement':[{'@type':'ListItem','position':1,'name':'Harness Library','item':SITE},{'@type':'ListItem','position':2,'name':e['name'] if e else 'Submit a harness' if path=='submit/' else 'About the library' if path=='about/' else title,'item':page_url}]}
        page['breadcrumb']={'@id':crumb['@id']};nodes.append(crumb)
    if e:
        work={'@type':'CreativeWork','@id':page_url+'#harness','name':e['name'],'description':e['summary'],'url':page_url,'sameAs':e['repository'],'version':e['version'],'genre':e['category'],'license':e['repository']+'/blob/main/LICENSE','encoding':{'@type':'MediaObject','contentUrl':e['distribution']['url']}}
        page['mainEntity']={'@id':work['@id']};nodes.append(work)
    return {'@context':'https://schema.org','@graph':nodes}

def metadata(path,title,description,structured,noindex=False):
    url=SITE+path;image=SITE+'assets/social-card.png'
    pieces=[f'<title>{h(title)}</title>',f'<meta name="description" content="{h(description)}">',
            f'<meta name="robots" content="{"noindex,follow" if noindex else "index,follow,max-image-preview:large"}">']
    if not noindex:
        pieces += [f'<link rel="canonical" href="{url}">',f'<link rel="alternate" type="text/markdown" href="{url}index.md">']
    pieces += [f'<link rel="describedby" href="{SITE}llms.txt">',f'<link rel="sitemap" type="application/xml" href="{SITE}sitemap.xml">',
               '<meta property="og:type" content="website">','<meta property="og:site_name" content="Harness Library">',
               f'<meta property="og:title" content="{h(title)}">',f'<meta property="og:description" content="{h(description)}">',
               f'<meta property="og:url" content="{url}">',f'<meta property="og:image" content="{image}">',
               '<meta property="og:image:width" content="1200">','<meta property="og:image:height" content="630">','<meta property="og:image:type" content="image/png">',
               '<meta property="og:image:alt" content="Harness Library: discover and share reusable AI agent harnesses">',
               '<meta name="twitter:card" content="summary_large_image">',f'<meta name="twitter:title" content="{h(title)}">',
               f'<meta name="twitter:description" content="{h(description)}">',f'<meta name="twitter:image" content="{image}">',
               '<script type="application/ld+json">'+json_script(structured)+'</script>']
    return '\n  '.join(pieces)

def markdown_entry(e):
    lines=[f'# {e["name"]}',f'\n> {e["summary"]}',f'\nCanonical page: {SITE}{harness_path(e)}',
           f'\nCategory: {e["category"]}\nVersion: {e["version"]}\nLicense: {e["license"]}',
           f'\nSource: {e["repository"]}\nDistribution: {e["distribution"]["url"]}\nScope: {e["distribution"]["scope"]}',
           '\n## Installation']
    for i,step in enumerate(e['installation']):
        lines += [f'\n### {i+1}. {step["title"]}',step['body']]
        if step.get('url'): lines.append(f'{step["label"]}: {step["url"]}')
        if step.get('command'):
            fence='`'*max(3,1+max(map(len,re.findall(r'`+',step['command'])),default=0))
            lines += [fence,step['command'],fence]
    for name,key in [('Manual setup','manual_setup'),('Additional notes','notes')]:
        lines.append('\n## '+name);lines.extend('- '+value for value in e[key]);
        if not e[key]:lines.append('None declared.')
    if e.get('contents'):
        lines.append('\n## Contents');lines.extend(f'- {key}: {", ".join(map(str,value)) if isinstance(value,list) else value}' for key,value in e['contents'].items())
    r=e['review'];lines += ['\n## Review scope',f'{r["status"]}; reviewed {r["reviewed_at"]}.',r['evidence'],f'Evidence source: {r["url"]}']
    if r['built_with_harneloop']:lines += ['\n## Built with Harneloop',e['harneloop']['detail'],e['harneloop']['url']]
    return '\n\n'.join(lines)+'\n'

def markdown_submit():
    parts=['# Submit an agent harness to Harness Library','\n> '+WELCOME,f'\nCanonical page: {SITE}submit/',f'\nSubmission form: {FORM}','No fork or pull request is required. A GitHub account is needed for the form.']
    for i,(title,body) in enumerate(SUBMIT_STEPS):parts += [f'\n## {i+1}. {title}',body]
    parts += ['\n## Before you submit','Bring repository, purpose/category, focused distribution/version/license, install steps and manual setup notes. Component counts and test evidence are optional. Harneloop is optional.']
    for q,answer in FAQ:parts += ['\n## '+q,answer]
    return '\n\n'.join(parts)+'\n'

def publish(root, destination, catalog):
    layout=(root/'site/layout.html').read_text(encoding='utf-8')
    entries=catalog['listings']
    home_md='# Harness Library\n\n> An open directory of reusable AI agent harnesses.\n\n'+DEFINITION+'\n\n'+WELCOME+'\n\n'
    home_md+='\n'.join(f'- [{e["name"]}]({SITE}{harness_path(e)}index.md): {e["summary"]}' for e in entries)
    home_md+=f'\n\nSubmit: {SITE}submit/index.md\nAbout: {SITE}about/index.md\nMachine-readable catalog: {SITE}catalog.json\n'
    about_md='# About Harness Library\n\n'+DEFINITION+'\n\nMaintained by Kristofer Jussmann (@Ker102): https://github.com/Ker102\n\nSource and review records: '+REPOSITORY+'\n\nHarneloop is optional. Setup reviews and artifact checks are scoped evidence, not universal model/platform certification.\n\n'
    about_md+='\n\n'.join('## '+q+'\n\n'+answer for q,answer in FAQ)+'\n'
    pages=[('', 'AI Agent Harness Directory | Harness Library','Discover reusable AI agent harnesses, skills and MCP workflows with clear installation and setup notes. New community submissions are welcome.',home(catalog),home_md,'CollectionPage',None),
           ('submit/','Submit an Agent Harness | Harness Library','New harness submissions are welcome. Share your GitHub repository and installation notes through a short form. No fork or pull request needed.',submission(),markdown_submit(),'WebPage',None),
           ('about/','What Is an Agent Harness? | Harness Library','Learn what agent harnesses include, how the library reviews submissions, and how reusable skills, tools and workflows fit together.',about(),about_md,'AboutPage',None)]
    for e in entries:
        pages.append((harness_path(e),e['name']+': Install & Setup | Harness Library',e['summary']+' Installation, manual setup, license and review scope in Harness Library.',detail(e),markdown_entry(e),'WebPage',e))
    def write_page(path,title,description,body,md,kind,e=None,noindex=False):
        content=layout.replace('@@METADATA@@',metadata(path,title,description,graph(path,title,description,entries,kind,e),noindex))
        content=content.replace('@@PAGE@@','home' if not path else 'detail' if e else path.split('/')[0])
        content=content.replace('@@BROWSE_CURRENT@@','aria-current="page"' if not path else '')
        content=content.replace('@@SUBMIT_CURRENT@@','aria-current="page"' if path=='submit/' else '')
        content=content.replace('@@CONTENT@@',body)
        target=destination/path;target.mkdir(parents=True,exist_ok=True)
        (target/'index.html').write_text(content,encoding='utf-8')
        if md:(target/'index.md').write_text(md,encoding='utf-8')
        return content
    for row in pages:write_page(*row)
    not_found=write_page('404/','Page Not Found | Harness Library','This page could not be found.',
                         '<section class="error"><h1>Page not found.</h1><p>This harness may have moved.</p>'+a('Browse the library →',BASE)+'</section>',None,'WebPage',noindex=True)
    (destination/'404.html').write_text(not_found,encoding='utf-8')
    # No lastmod: a routine badge check does not mean the content was updated.
    ET.register_namespace('', 'http://www.sitemaps.org/schemas/sitemap/0.9')
    sitemap=ET.Element('{http://www.sitemaps.org/schemas/sitemap/0.9}urlset')
    for path,*_ in pages:
        row=ET.SubElement(sitemap,'{http://www.sitemaps.org/schemas/sitemap/0.9}url');ET.SubElement(row,'{http://www.sitemaps.org/schemas/sitemap/0.9}loc').text=SITE+path
    ET.ElementTree(sitemap).write(destination/'sitemap.xml',encoding='utf-8',xml_declaration=True)
    llms='# Harness Library\n\n> Open directory of reusable AI agent harnesses, with focused distributions and clear setup instructions.\n\n'+DEFINITION+'\n\nNew community submissions are welcome. Harneloop is optional. Review labels describe specific evidence; they do not guarantee every model/platform.\n\n## Directory\n'
    llms+=f'- [Catalog]({SITE}index.md): Overview and available harnesses.\n- [About the library]({SITE}about/index.md): Definitions, maintainer, review scope and FAQ.\n- [Submit a harness]({SITE}submit/index.md): Short issue-first submission process.\n'
    llms+='\n## Harness installation guides\n'+'\n'.join(f'- [{e["name"]}]({SITE}{harness_path(e)}index.md): {e["summary"]}' for e in entries)
    llms+=f'\n\n## Data\n- [Machine-readable catalog]({SITE}catalog.json): Reviewed listings with source, distribution, install steps, manual setup, license and evidence.\n- [Full text]({SITE}llms-full.txt): Combined public guide and installation text.\n'
    (destination/'llms.txt').write_text(llms,encoding='utf-8')
    (destination/'llms-full.txt').write_text(home_md+'\n\n'+markdown_submit()+'\n\n'+about_md+'\n\n'+'\n\n'.join(markdown_entry(e) for e in entries),encoding='utf-8')
    (destination/'robots.txt').write_text('# Project-site reference only: crawlers read the host-root /robots.txt.\n# Host-root currently returns 404, which does not restrict crawling.\nUser-agent: *\nAllow: /harness-library/\nSitemap: '+SITE+'sitemap.xml\n',encoding='utf-8')
    return pages
