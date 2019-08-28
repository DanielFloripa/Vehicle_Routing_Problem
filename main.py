from truck import Truck
from cargo import Cargo
from helper import LoadData
from numpy import inf


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


if __name__ == "__main__":

    cargos = LoadData(Cargo, "files/cargo.csv")
    trucks = LoadData(Truck, "files/trucks.csv")
    all_distances = {}

    for cargo in cargos.list:
        distances = []
        winner = inf
        for truck in trucks.list:
            dist = truck.get_distance(truck.origin, cargo.origin, cargo.destination)
            if dist < winner:
                winner = dist
                cargo.can_be_carried_by = truck
                cargo.will_travel = dist
            distances.append(dist)
        print(f"{cargo.uniq_id}: {cargo.can_be_carried_by.uniq_id} {cargo.will_travel}")
        distances.sort()
        all_distances[f'{cargo.uniq_id}'] = distances

    print(all_distances)
