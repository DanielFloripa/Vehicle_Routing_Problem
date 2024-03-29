import json
from copy import deepcopy


class FreightBroker:
    def __init__(self, cargos, trucks, truck_returns_to_home=False):
        self.cargos = deepcopy(cargos)
        self.trucks = deepcopy(trucks)
        self.truck_returns = truck_returns_to_home
        self.all_distances = {}

    def map_cargo_to_trucks(self):
        """
        Main algorithm:
        Time and space complexity is O(n^2)
        :return:
        """
        for cargo in self.cargos:
            for truck in self.trucks:

                actual_distance = truck.will_travel_to(
                    cargo.origin,
                    cargo.destination,
                    truck_returns=self.truck_returns)

                if actual_distance < cargo.shortest_distance:
                    cargo.truck_booking = truck
                    cargo.shortest_distance = actual_distance

                cargo.all_potential_distances.append({'id': truck.id, 'distance': actual_distance})
            self.trucks.remove(cargo.truck_booking)

            self.all_distances[cargo.id] = sorted(cargo.all_potential_distances, key=lambda l: l['distance'])

    def print_cargo_map(self):
        for cargo in self.cargos:
            print(f"Cargo {cargo.id} "
                  f"will be carried by {cargo.truck_booking.id}"
                  f"and will travel: {cargo.shortest_distance}")

    def print_all_distances(self):
        print("\nAll possible distances are: ")
        for k, v in self.all_distances.items():
            print(f"Cargo {k}: {v}")

    def save_results(self):
        with open('files/data.json', 'w') as outfile:
            json.dump(self.all_distances, outfile)
