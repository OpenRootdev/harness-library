import sys
import shutil
import tempfile
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import catalog as c
import notify_indexnow as n

def sitemap(url):
    return '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>'+url+'</loc></url></urlset>'

class DiscoveryTests(unittest.TestCase):
    def test_notification_scope_cannot_escape_the_project(self):
        for url in ['https://example.com/','https://ker102.github.io/other/','https://openrootdev.github.io/harness-library/../other/','https://openrootdev.github.io/harness-library/%2e%2e/other/','https://openrootdev.github.io/harness-library/#private','https://openrootdev.github.io/harness-library/?secret=value']:
            with self.assertRaises(ValueError):n.payload(sitemap(url),'abcdefgh12345678')
        result=n.payload(sitemap(c.SITE),'abcdefgh12345678')
        self.assertEqual(result['urlList'],[c.SITE]);self.assertEqual(result['keyLocation'],c.SITE+n.KEY_FILE)
    def test_empty_catalog_is_not_notified(self):
        with self.assertRaises(ValueError):n.payload('<urlset/>','abcdefgh12345678')
    def test_ownership_files_survive_build_without_becoming_sitemap_pages(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory)
            shutil.copytree(c.ROOT/'site',root/'site');shutil.copytree(c.ROOT/'data',root/'data')
            name='google-example.html';content='google-site-verification: '+name
            (root/'site'/name).write_text(content,encoding='utf-8')
            c.build(root)
            self.assertEqual((root/'dist'/name).read_text(encoding='utf-8'),content)
            self.assertEqual((root/'dist'/n.KEY_FILE).read_text(encoding='utf-8'),(root/'site'/n.KEY_FILE).read_text(encoding='utf-8'))
            self.assertFalse((root/'dist/layout.html').exists())
            xml=(root/'dist/sitemap.xml').read_text(encoding='utf-8');self.assertNotIn(name,xml);self.assertNotIn(n.KEY_FILE,xml)

if __name__=='__main__':unittest.main()
