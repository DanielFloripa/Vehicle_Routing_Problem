from truck import Truck
from cargo import Cargo
from load_data import LoadData


def get_map_cargo_truck(truck_returns=False):
    all_distances = {}
    list_cargos = cargos.list[:]
    list_trucks = trucks.list[:]

    for cargo in list_cargos:
        for truck in list_trucks:
            dist = truck.move_truck_to(cargo.origin, cargo.destination, truck_returns=truck_returns)
            if dist < cargo.will_travel_shortest_distance:
                cargo.can_be_carried_by = truck
                cargo.will_travel_shortest_distance = dist
            cargo.potential_distances.append(dist)
        list_trucks.remove(cargo.can_be_carried_by)
        print(f"Cargo {cargo.uniq_id} will be carried by {cargo.can_be_carried_by.uniq_id} and will travel: {cargo.will_travel_shortest_distance}")
        cargo.potential_distances.sort()
        all_distances[cargo.uniq_id] = cargo.potential_distances
    return list_cargos, all_distances


if __name__ == "__main__":

    cargos = LoadData(Cargo, "files/cargo.csv")
    trucks = LoadData(Truck, "files/trucks.csv")

    print("\nBest map between cargo and trucks (truck returns to origin)")
    map_match_with_truck_returns, distances_with_returns = get_map_cargo_truck(truck_returns=True)

    print("\nBest map between cargo and trucks (truck don't returns to origin)")
    map_match, distances = get_map_cargo_truck()

    print("\nAll possible distances is: ")
    for k, v in distances.items():
        print(k, v)
