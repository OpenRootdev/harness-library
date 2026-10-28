import copy
import sys
import tempfile
import shutil
import unittest
from pathlib import Path
from urllib.parse import urlsplit, parse_qs

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import catalog as c
import publishing as p
from site_config import FORM
from stage_cloudrun import stage


class ToolIndexTests(unittest.TestCase):
    def test_deployment_context_excludes_private_and_stale_output(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for name in ('site', 'data', 'deploy'):
                shutil.copytree(c.ROOT / name, root / name)
            (root / 'docs/internal').mkdir(parents=True)
            (root / 'docs/internal/private.json').write_text('private')
            (root / 'dist').mkdir()
            (root / 'dist/stale-secret.txt').write_text('private')
            target = stage(root)
            self.assertTrue((target / 'public/index.html').is_file())
            self.assertFalse((target / 'public/stale-secret.txt').exists())
            self.assertFalse((target / 'docs').exists())
            self.assertEqual({p.name for p in target.iterdir()}, {'public', 'Dockerfile', 'nginx.conf'})

    def test_hosted_submission_composes_a_tool_issue_without_unpublished_template(self):
        url = urlsplit(FORM)
        self.assertEqual(url.netloc, 'github.com')
        self.assertEqual(url.path, '/OpenRootdev/toolindex/issues/new')
        query = parse_qs(url.query)
        self.assertNotIn('template', query)
        self.assertIn('Logo or custom image (optional)', query['body'][0])
        self.assertIn('Do not include secrets.', query['body'][0])

    def test_api_with_non_github_source_and_no_image_is_valid(self):
        entry = copy.deepcopy(c.entries()[0])
        entry['type'] = 'API'
        entry['repository'] = 'https://example.org/docs'
        entry['distribution'] = dict(kind='api', url='https://example.org/api',
                                     label='API documentation', scope='Hosted API, account required',
                                     repository_has_extra_material=False)
        entry['license'] = 'Commercial service terms'
        entry['version'] = 'Rolling service'
        entry.pop('image', None)
        c.validate_entry(entry)
        entry.update(review=dict(built_with_harneloop=False), boost=None)
        html = p.listing(entry)
        self.assertIn('data-type="API"', html)
        self.assertIn('tool-initials', html)
        self.assertNotIn('<img', html)
        self.assertIn('https://example.org/docs', html)

    def test_unsafe_optional_image_or_unknown_type_is_rejected(self):
        for url in ['javascript:alert(1)', 'data:image/svg+xml,x', 'assets/logos/../../x.svg',
                    'https://user:secret@example.org/logo.png']:
            entry = copy.deepcopy(c.entries()[0])
            entry['image'] = dict(url=url, alt='Logo', source='https://example.org/logo')
            with self.assertRaises(ValueError):
                c.validate_entry(entry)
        entry = copy.deepcopy(c.entries()[0]);entry['type'] = '<script>'
        with self.assertRaises(ValueError):
            c.validate_entry(entry)

    def test_toolindex_badge_and_all_previous_hosts_are_accepted(self):
        slug = c.entries()[0]['id']
        for site in [c.SITE, *c.LEGACY_SITES]:
            for name in ['Listed in ToolIndex', 'Listed in Harness Library']:
                for route in ['tools/', 'harnesses/']:
                    badge = f'[![{name}]({site}badges/{slug}.svg)]({site}{route}{slug}/)'
                    self.assertTrue(c.has_badge(badge, slug))

    def test_legacy_route_redirects_to_new_canonical_without_entering_sitemap(self):
        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory)
            catalog = c.checked_catalog()
            p.publish(c.ROOT, destination, catalog)
            for entry in catalog['listings']:
                html = (destination/'harnesses'/entry['id']/'index.html').read_text(encoding='utf-8')
                self.assertIn('https://toolindex.org/tools/'+entry['id']+'/', html)
                self.assertIn('noindex,follow', html)
            self.assertNotIn('/harnesses/', (destination/'sitemap.xml').read_text(encoding='utf-8'))
            home = (destination/'index.html').read_text(encoding='utf-8')
            self.assertIn('id="tool-type"', home)
            self.assertNotIn('@@', home)
            self.assertIn('https://github.com/OpenRootdev/toolindex/blob/main/docs/badge-program.md', home)


if __name__ == '__main__':
    unittest.main()
