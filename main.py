from truck import Truck
from cargo import Cargo
from helper import LoadData


"""Given a list of trucks and their current locations and a list of cargos and their pickup and
delivery locations, find the optimal mapping of trucks to cargos to minimize the overall distances
the trucks must travel.
Please assume that each truck can only carry up to one cargo, each truck can only make up to
one trip and that some trucks may not be used at all.
Here are 2 csv files for you to complete the assignment: cargo.csv and trucks.csv. Cargo.csv is
a list of cargos we need to move (with product name, origin and destination city) and trucks.csv
is a list of trucks and their home city.
Please insert a comment (or docstring) at the beginning of the file (before line 5) saying which
Python version you have used (e.g.: 2.7, 3.6, etc)"""


def get_map_cargo_truck(truck_returns=False):
    all_distances = {}
    list_cargos = cargos[:]
    list_trucks = trucks[:]

    for cargo in list_cargos:
        for truck in list_trucks:
            dist = truck.get_distance(truck.origin, cargo.origin, cargo.destination, truck_returns=truck_returns)
            if dist < cargo.will_travel_shortest_distance:
                cargo.can_be_carried_by = truck
                cargo.will_travel_shortest_distance = dist
            cargo.potential_distances.append(dist)
        list_trucks.remove(cargo.can_be_carried_by)
        print(
            f"Cargo: {cargo.uniq_id} will be carried by {cargo.can_be_carried_by.uniq_id} and will travel: {cargo.will_travel_shortest_distance}")
        cargo.potential_distances.sort()
        all_distances[cargo.uniq_id] = cargo.potential_distances
    return list_cargos, all_distances


if __name__ == "__main__":

    cargos = LoadData(Cargo, "files/cargo.csv").list
    trucks = LoadData(Truck, "files/trucks.csv").list

    print("\nBest map between cargo and trucks (truck dont returns to origin)")
    map_match, distances = get_map_cargo_truck()

    print("\nBest map between cargo and trucks (truck returns to origin)")
    map_match_with_truck_returns, distances_with_returns = get_map_cargo_truck(truck_returns=True)

    print("\nAll possible distances is: ")
    for k, v in distances.items():
        print(k, v)
