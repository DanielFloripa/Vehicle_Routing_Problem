from src.freight_broker import FreightBroker
from src.load_data import LoadData
from src.truck import Truck
from src.cargo import Cargo

"""
Using python3.6 in this development
"""

if __name__ == "__main__":

    cargos = LoadData(Cargo, "files/cargo.csv")
    trucks = LoadData(Truck, "files/trucks.csv")

    print("\nBest map between cargo and trucks (truck returns to origin)")
    loadsmart_truck_returns = FreightBroker(cargos.list, trucks.list, truck_returns_to_home=True)

    loadsmart_truck_returns.map_cargo_to_trucks()
    loadsmart_truck_returns.print_cargo_map()

    print("\nBest map between cargo and trucks (truck don't returns to origin)")
    loadsmart = FreightBroker(cargos.list, trucks.list)

    loadsmart.map_cargo_to_trucks()
    loadsmart.print_cargo_map()

    # With this method you can print all distances:
    # loadsmart.print_all_distances()
