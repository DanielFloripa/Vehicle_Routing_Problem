import unittest
from src.truck import Truck
from src.cargo import Cargo
from src.freight_broker import FreightBroker
from src.load_data import LoadData


class UnitTests(unittest.TestCase):

    def test_load_data_from_file(self):
        """
        Just load the file and test if the first product is
        'Light bulbs' and the last is 'Oranges'
        """
        cargos = LoadData(Cargo, "files/cargo.csv")
        self.assertEqual(cargos.list[0].name, "Light bulbs", msg=self.test_load_data_from_file.__doc__)
        self.assertEqual(cargos.list[-1].name, "Oranges", msg=self.test_load_data_from_file.__doc__)

    def test_sample_distance_euclidean_distance(self):
        """
        Euclidean distance between (2,-1) and (-2,2) == 5.0
        Sample data and result is based on:
        https://www.cut-the-knot.org/pythagoras/DistanceFormula.shtml
        """
        object1 = Truck(['a1', 'b1', 'c1', 2, -1])
        object2 = Cargo(['a2', 'b2', 'c2', -2, 2])
        distance = object1.euclidean_distance(object2.destination)
        self.assertEqual(distance, 5.0, msg=self.test_sample_distance_euclidean_distance.__doc__)


class IntegrationTests(unittest.TestCase):

    def setUp(self):
        self.cargos = LoadData(Cargo, "files/cargo.csv")
        self.trucks = LoadData(Truck, "files/trucks.csv")

    def test_route_pickup_cargo_deliver_cargo(self):
        """
        Example from list index 1 when truck don't returns to home:
        Cargo Recyclables__VA will be carried by
        Ricardo_Juradoacramento__VA and
        will travel: 10.376996409265375
        """
        loadsmart = FreightBroker(self.cargos.list, self.trucks.list)
        loadsmart.map_cargo_to_trucks()
        self.assertEqual(loadsmart.cargos[1].id, "Recyclables__VA")
        self.assertEqual(loadsmart.cargos[1].shortest_distance, 10.376996409265375)

    def test_route_pickup_cargo_deliver_cargo_and_truck_returns_to_home(self):
        """
        Example from list index 1 when truck returns to home:
        Cargo Recyclables__VA will be carried by
        Jorge_L_Denisollywood__COand and
        will travel: 77.59998023656951
        """
        loadsmart = FreightBroker(self.cargos.list, self.trucks.list, truck_returns_to_home=True)
        loadsmart.map_cargo_to_trucks()
        self.assertEqual(loadsmart.cargos[2].id, 'Apples__OH')
        self.assertEqual(loadsmart.cargos[2].shortest_distance, 77.59998023656951)

    def test_all_potential_distances_from_all_cargos(self):
        """
        Taking the results of a run without truck returns to home as an example,
        compare all possible distances saved in file 'results.json'
        """
        loadsmart = FreightBroker(self.cargos.list, self.trucks.list)
        loadsmart.map_cargo_to_trucks()

        results_from_file = LoadData(dict, "files/results.json").dict

        self.assertDictEqual(loadsmart.all_distances, results_from_file)


if __name__ == '__main__':
    unittest.main()
