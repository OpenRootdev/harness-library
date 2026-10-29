import copy
import sys
import unittest
from datetime import datetime, timedelta
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import catalog as c

class CatalogTests(unittest.TestCase):
    def setUp(self):
        self.entry=c.entries()[0]
        self.now=datetime(2026,10,10,12,tzinfo=c.UTC)
        self.badge=f'[![Listed in Harness Library]({c.SITE}badges/{self.entry["id"]}.svg)]({c.SITE}#{self.entry["id"]})'
    def test_seed_entries_valid(self):
        self.assertEqual(len(c.checked_catalog()['listings']),len(c.entries()))
    def test_install_and_manual_setup_are_required(self):
        for field in ['installation','manual_setup']:
            e=copy.deepcopy(self.entry);e.pop(field)
            with self.assertRaises(ValueError):c.validate_entry(e)
    def test_mixed_repo_needs_focused_distribution(self):
        e=copy.deepcopy(self.entry);e['distribution']['kind']='focused-repository'
        with self.assertRaisesRegex(ValueError,'Mixed'):c.validate_entry(e)
    def test_cannot_award_review_or_boost_in_submission(self):
        for key in ['review','boost','verified','built_with_harneloop']:
            e=copy.deepcopy(self.entry);e[key]=True
            with self.assertRaises(ValueError):c.validate_entry(e)
    def test_unsafe_links_are_rejected(self):
        for url in ['javascript:alert(1)','http://example.com','https://user:secret@example.com','https://example.com/x\ny']:
            e=copy.deepcopy(self.entry);e['distribution']['url']=url
            with self.assertRaises(ValueError):c.validate_entry(e)
    def test_badge_needs_exact_image_backlink_and_top_placement(self):
        self.assertTrue(c.has_badge('# Name\n'+self.badge,self.entry['id']))
        self.assertFalse(c.has_badge(self.badge.replace('#'+self.entry['id'],'#other'),self.entry['id']))
        self.assertFalse(c.has_badge('\n'*31+self.badge,self.entry['id']))
        self.assertFalse(c.has_badge('```md\n'+self.badge+'\n```',self.entry['id']))
        self.assertFalse(c.has_badge('<!--'+self.badge+'-->',self.entry['id']))
        self.assertFalse(c.has_badge('<!--\n'+self.badge+'\n'*30+'-->',self.entry['id']))
        self.assertFalse(c.has_badge('<!--\n'+'comment\n'*32+'-->\n'+self.badge,self.entry['id']))
        self.assertFalse(c.has_badge('`'+self.badge+'`',self.entry['id']))
    def test_actual_html_badge_is_supported(self):
        slug=self.entry['id'];html=f'<p><a href="{c.SITE}#{slug}"><img src="{c.SITE}badges/{slug}.svg" alt="Listed in Harness Library"></a></p>'
        self.assertTrue(c.has_badge(html,slug))
    def test_owner_migration_preserves_legacy_badge_and_grant(self):
        slug=self.entry['id'];old='https://kaelux-labs.github.io/harness-library/'
        legacy=f'[![Listed in Harness Library]({old}badges/{slug}.svg)]({old}#{slug})'
        receipt={'grants':{}};fetch=lambda e:(legacy,e['repository']+'/blob/main/README.md')
        c.refresh([self.entry],receipt,self.now,fetch)
        original=receipt['grants'][slug]['expires_at']
        c.refresh([self.entry],receipt,self.now+timedelta(days=2),lambda e:(self.badge,e['repository']+'/blob/main/README.md'))
        self.assertEqual(receipt['grants'][slug]['expires_at'],original)
        self.assertTrue(c.active(receipt['grants'][slug],self.now+timedelta(days=2)))
    def test_boost_expires_at_exactly_14_days_and_does_not_renew(self):
        receipt={'grants':{}};fetch=lambda e:(self.badge,e['repository']+'/blob/main/README.md')
        c.refresh([self.entry],receipt,self.now,fetch);grant=receipt['grants'][self.entry['id']]
        self.assertTrue(c.active(grant,self.now));c.validate_grants(receipt['grants'])
        original=grant['expires_at'];end=self.now+timedelta(days=14)
        c.refresh([self.entry],receipt,end,fetch)
        self.assertFalse(c.active(grant,end));self.assertEqual(grant['expires_at'],original)
    def test_removing_and_readding_badge_does_not_reset_window(self):
        r={'grants':{}};fetch=lambda e:(self.badge,e['repository']+'/blob/main/README.md')
        c.refresh([self.entry],r,self.now,fetch);g=r['grants'][self.entry['id']];initial=g['granted_at']
        c.refresh([self.entry],r,self.now+timedelta(days=1),lambda e:('',e['repository']+'/blob/main/README.md'))
        self.assertFalse(c.active(g,self.now+timedelta(days=1)))
        c.refresh([self.entry],r,self.now+timedelta(days=2),fetch)
        self.assertEqual(g['granted_at'],initial);self.assertTrue(c.active(g,self.now+timedelta(days=2)))
    def test_stale_or_future_badge_check_cannot_rank_as_active(self):
        r={'grants':{}};c.refresh([self.entry],r,self.now,lambda e:(self.badge,e['repository']+'/blob/main/README.md'));g=r['grants'][self.entry['id']]
        self.assertFalse(c.active(g,self.now+timedelta(hours=49)));self.assertFalse(c.active(g,self.now-timedelta(seconds=1)))
        g['expires_at']=c.iso(self.now+timedelta(days=15))
        with self.assertRaises(ValueError):c.validate_grants(r['grants'])
    def test_network_failure_does_not_invent_a_badge(self):
        def fail(e):raise TimeoutError()
        receipt=c.refresh([self.entry],{'grants':{}},self.now,fail)
        self.assertEqual(receipt['grants'],{})

if __name__=='__main__':unittest.main()
