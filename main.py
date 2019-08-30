from load_data import LoadData
from truck import Truck
from cargo import Cargo
from freight_broker import FreightBroker


if __name__ == "__main__":

    cargos = LoadData(Cargo, "files/cargo.csv")
    trucks = LoadData(Truck, "files/trucks.csv")

    print("\nBest map between cargo and trucks (truck returns to origin)")
    loadsmart_truck_returns = FreightBroker(cargos.list, trucks.list, truck_returns_to_home=True)

    loadsmart_truck_returns.map_cargo_to_trucks()
    loadsmart_truck_returns.print_cargo_map()
    loadsmart_truck_returns.print_all_distances()

    print("\nBest map between cargo and trucks (truck don't returns to origin)")
    loadsmart = FreightBroker(cargos.list, trucks.list)

    loadsmart.map_cargo_to_trucks()
    loadsmart.print_cargo_map()
    loadsmart.print_all_distances()
