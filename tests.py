import unittest
from truck import Truck
from cargo import Cargo


class MyTestCase(unittest.TestCase):
    def test_sample_distance(self):
        """ Data and result is based on:
            https://www.cut-the-knot.org/pythagoras/DistanceFormula.shtml"""
        object1 = Truck(['name1', 'city1', 'state1', 2, -1])
        object2 = Truck(['name2', 'city2', 'state2', -2, 2])
        distance = object1.euclidean_distance(object2.destination)
        self.assertEqual(distance, 5.0)

    def test_truck_route_pickup_cargo_deliver_cargo(self):
        self.assertEqual(True, False)

    def test_truck_route_pickup_cargo_deliver_cargo_come_back(self):
        self.assertEqual(True, False)

    def test_load_data_from_file(self):
        self.assertEqual(True, False)

    def test_get_map_cargo_truck(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
