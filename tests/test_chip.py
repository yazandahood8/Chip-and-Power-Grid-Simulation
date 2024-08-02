# tests/test_chip.py

import unittest
from src.chip import Chip
from src.gates import Gate

class TestChip(unittest.TestCase):
    def setUp(self):
        self.chip = Chip()
        self.gate1 = Gate("Gate1", 1)
        self.gate2 = Gate("Gate2", 2)
        self.chip.add_gate(self.gate1)
        self.chip.add_gate(self.gate2)
        self.gate1.set_output(self.gate2)

    def test_calculate_delays(self):
        self.assertEqual(self.chip.calculate_delays(), {'Gate1': 1, 'Gate2': 2})

    def test_find_critical_path(self):
        self.assertEqual(self.chip.find_critical_path(), ('Gate2', 2))

    def test_edge_case(self):
        chip_empty = Chip()
        self.assertEqual(chip_empty.calculate_delays(), {})
        self.assertEqual(chip_empty.find_critical_path(), (None, -1))

if __name__ == '__main__':
    unittest.main()
