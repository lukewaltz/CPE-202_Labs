import unittest
from location import *


class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc), "Location('SLO', 35.3, -120.7)")

    # Add more tests!
    def test_eq_SLO_SLO(self):
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location("SLO", 35.3, -120.7)
        self.assertEqual(loc1, loc2)

    def test_eq_SLO_Paris(self):
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location("Paris", 48.9, 2.4)
        self.assertNotEqual(loc1, loc2)

    def test_eq_Paris_SLO(self):
        loc1 = Location("Paris", 48.9, 2.4)
        loc2 = Location("SLO", 35.3, -120.7)
        self.assertNotEqual(loc1, loc2)

    def test_eq_Paris_Paris(self):
        loc1 = Location("Paris", 48.9, 2.4)
        loc2 = Location("Paris", 48.9, 2.4)
        self.assertEqual(loc1, loc2)

    def test_init_name(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(loc.name, "SLO")

    def test_init_lat(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(loc.lat, 35.3)

    def test_init_lon(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(loc.lon, -120.7)


if __name__ == "__main__":
    unittest.main()
