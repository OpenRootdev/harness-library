import copy
import json
import sys
import tempfile
import unittest
from html.parser import HTMLParser
from pathlib import Path
from xml.etree import ElementTree as ET
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import catalog as c
import publishing as p

class Page(HTMLParser):
    def __init__(self, source):
        super().__init__();self.canonical=[];self.meta={};self.h1=0;self.scripts=[];self.current_script=None;self.hrefs=[];self.data=[]
        self.feed(source)
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='h1':self.h1+=1
        if tag=='link' and a.get('rel')=='canonical':self.canonical.append(a['href'])
        if tag=='meta':self.meta[a.get('name',a.get('property',''))]=a.get('content')
        if tag=='a':self.hrefs.append(a.get('href'))
        if tag=='script':self.current_script={'type':a.get('type'),'src':a.get('src'),'text':''};self.scripts.append(self.current_script)
    def handle_endtag(self,tag):
        if tag=='script':self.current_script=None
    def handle_data(self,data):
        self.data.append(data)
        if self.current_script:self.current_script['text']+=data

class PublishingTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.out=Path(self.temp.name);self.catalog=c.checked_catalog();p.publish(c.ROOT,self.out,self.catalog)
    def tearDown(self):self.temp.cleanup()
    def test_install_details_are_in_initial_html_without_javascript(self):
        for e in self.catalog['listings']:
            source=(self.out/p.harness_path(e)/'index.html').read_text(encoding='utf-8');page=Page(source);text=' '.join(page.data)
            self.assertIn(e['name'],text)
            for step in e['installation']:self.assertIn(step['body'],text)
            for note in e['manual_setup']:self.assertIn(note,text)
            self.assertIn(e['review']['evidence'],text)
            self.assertEqual(page.h1,1)
    def test_each_page_has_one_unique_canonical_and_matching_jsonld(self):
        canonical=[]
        for source in [self.out/'index.html',self.out/'submit/index.html',self.out/'about/index.html',*[self.out/p.harness_path(e)/'index.html' for e in self.catalog['listings']]]:
            page=Page(source.read_text(encoding='utf-8'));self.assertEqual(len(page.canonical),1);canonical+=page.canonical
            self.assertNotIn('noindex',page.meta['robots']);self.assertEqual(page.h1,1)
            graph=json.loads(next(s['text'] for s in page.scripts if s['type']=='application/ld+json'))['@graph']
            self.assertTrue(any(n.get('url')==page.canonical[0] and n['@type'] in ['WebPage','CollectionPage','AboutPage'] for n in graph))
            self.assertIn('og:image',page.meta)
        self.assertEqual(len(canonical),len(set(canonical)))
    def test_home_links_are_real_paths_and_submissions_are_prominent(self):
        page=Page((self.out/'index.html').read_text(encoding='utf-8'))
        for e in self.catalog['listings']:self.assertIn(p.local(p.harness_path(e)),page.hrefs)
        self.assertIn('/submit/',page.hrefs)
        self.assertIn('New submissions welcome',' '.join(page.data))
    def test_sitemap_contains_only_existing_canonical_pages(self):
        root=ET.parse(self.out/'sitemap.xml').getroot();locations=[el.text for el in root.iter('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
        n=3+len(self.catalog['listings']);self.assertEqual(len(locations),n);self.assertEqual(len(set(locations)),n)
        for url in locations:
            self.assertNotIn('#',url);self.assertTrue((self.out/url.removeprefix(p.SITE)/'index.html').is_file())
    def test_json_and_html_escape_submitted_script_content(self):
        catalog=copy.deepcopy(self.catalog);catalog['listings'][0]['summary']='</script><img src=x onerror=alert(1)>'
        p.publish(c.ROOT,self.out,catalog);source=(self.out/p.harness_path(catalog['listings'][0])/'index.html').read_text(encoding='utf-8')
        self.assertIn('&lt;/script&gt;&lt;img',source);self.assertNotIn('<img src=x',source)
        graph=next(s['text'] for s in Page(source).scripts if s['type']=='application/ld+json')
        parsed=json.loads(graph);self.assertEqual(next(n for n in parsed['@graph'] if n['@type']=='CreativeWork')['description'],catalog['listings'][0]['summary'])
    def test_agent_resources_match_installation_and_review_scope(self):
        llms=(self.out/'llms.txt').read_text(encoding='utf-8');full=(self.out/'llms-full.txt').read_text(encoding='utf-8')
        for e in self.catalog['listings']:
            self.assertIn(p.SITE+p.harness_path(e)+'index.md',llms)
            md=(self.out/p.harness_path(e)/'index.md').read_text(encoding='utf-8');self.assertIn(e['distribution']['url'],md)
            self.assertIn(e['review']['evidence'],md);self.assertIn(e['review']['evidence'],full)
        self.assertIn('No fork or pull request',full)
    def test_unknown_pages_are_noindex(self):
        source=Page((self.out/'404.html').read_text(encoding='utf-8'));self.assertIn('noindex',source.meta['robots']);self.assertEqual(source.canonical,[])
    def test_canonical_and_legacy_badge_links_both_qualify(self):
        e=self.catalog['listings'][0];slug=e['id'];image=p.SITE+'badges/'+slug+'.svg'
        for target in [p.SITE+'#'+slug,p.SITE+p.harness_path(e)]:
            self.assertTrue(c.has_badge(f'[![Listed in Harness Library]({image})]({target})',slug))

if __name__=='__main__':unittest.main()
