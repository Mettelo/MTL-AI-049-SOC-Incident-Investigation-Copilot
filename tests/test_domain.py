import copy,json,unittest
from pathlib import Path
from engine import build

class SOCCases(unittest.TestCase):
    def setUp(self): self.data=json.loads(Path('data/reference/demo.json').read_text())
    def test_reversed_input_is_chronological(self):
        self.data['events'].reverse();d=build(self.data)
        times=[r['details']['timestamp'] for r in d['records'] if r['kind']=='observed_event']
        self.assertEqual(times,sorted(times))
    def test_unknown_behaviour_has_no_mapping(self):
        for e in self.data['events']:e['event_type']='unknown'
        self.assertFalse(any(r['kind']=='attack_hypothesis' for r in build(self.data)['records']))
    def test_duplicate_event_rejected(self):
        self.data['events'].append(copy.deepcopy(self.data['events'][0]))
        with self.assertRaises(AssertionError):build(self.data)
    def test_timezone_required(self):
        self.data['events'][0]['timestamp']='2025-01-01T10:00:00'
        with self.assertRaises(AssertionError):build(self.data)
    def test_frozen_scenarios_grounded(self):
        from app import validate
        for p in Path('data/reference/scenarios').glob('*.json'):
            d=build(json.loads(p.read_text()));self.assertTrue(validate(d))
            self.assertFalse(any('confirmed compromise' in r['text'].lower() for r in d['records']))
