import unittest
from truck import Truck
from cargo import Cargo
from freight_broker import FreightBroker
from load_data import LoadData


class MyTestCase(unittest.TestCase):
    def test_sample_distance_euclidean_distance(self):
        """
        Sample data and result is based on:
            https://www.cut-the-knot.org/pythagoras/DistanceFormula.shtml
        """
        object1 = Truck(['name1', 'city1', 'state1', 2, -1])
        object2 = Cargo(['name2', 'city2', 'state2', -2, 2])
        distance = object1.euclidean_distance(object2.destination)
        self.assertEqual(distance, 5.0)

    def test_load_data_from_file(self):
        cargos = LoadData(Cargo, "files/cargo.csv")
        self.assertEqual(cargos.list[0].name, "Light bulbs")

    def test_route_pickup_cargo_deliver_cargo(self):
        """
        Example from list index 1:
            Cargo Recyclables__VA will be carried by
            Ricardo_Juradoacramento__VA and
            will travel: 10.376996409265375
        """
        cargos = LoadData(Cargo, "files/cargo.csv")
        trucks = LoadData(Truck, "files/trucks.csv")

        loadsmart = FreightBroker(cargos.list, trucks.list)
        loadsmart.map_cargo_to_trucks()

        self.assertEqual(loadsmart.cargos[1].shortest_distance, 10.376996409265375)

    def test_route_pickup_cargo_deliver_cargo_and_truck_returns_to_home(self):
        """
        Example from list index 1:
           Cargo Recyclables__VA will be carried by
           Paul_J_Krez_Companyorton_Grove__NC and
           will travel: 17.47186153481572
        """
        cargos = LoadData(Cargo, "files/cargo.csv")
        trucks = LoadData(Truck, "files/trucks.csv")

        loadsmart = FreightBroker(cargos.list, trucks.list, truck_returns_to_home=True)
        loadsmart.map_cargo_to_trucks()

        self.assertEqual(loadsmart.cargos[1].shortest_distance, 17.47186153481572)

    def test_all_potential_distances_from_all_cargos(self):
        cargos = LoadData(Cargo, "files/cargo.csv")
        trucks = LoadData(Truck, "files/trucks.csv")

        loadsmart = FreightBroker(cargos.list, trucks.list)
        loadsmart.map_cargo_to_trucks()

        results = LoadData(dict, "files/results.json").dict

        self.assertDictEqual(loadsmart.all_distances, results)

        #for product, potential_distance in loadsmart.all_distances:
        #    print(product, potential_distance)


if __name__ == '__main__':
    unittest.main()
