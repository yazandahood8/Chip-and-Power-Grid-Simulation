# tests/test_power_grid.py

import unittest
from src.power_grid import PowerGrid

class TestPowerGrid(unittest.TestCase):
    def setUp(self):
        self.power_grid = PowerGrid(10)
        self.power_grid.apply_current(5, 5, 0.2)

    def test_calculate_ir_drop(self):
        min_ir, max_ir = self.power_grid.calculate_ir_drop()
        self.assertGreaterEqual(max_ir, min_ir)

    def test_simulate_em(self):
        em_affected_areas = self.power_grid.simulate_em()
        self.assertIn(5, em_affected_areas[0])
        self.assertIn(5, em_affected_areas[1])

if __name__ == '__main__':
    unittest.main()
