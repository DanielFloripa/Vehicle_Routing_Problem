# Assessment test

## Problem description:
Given a list of trucks and their current locations and a list of cargos and their pickup and delivery locations, find the optimal mapping of trucks to cargos to minimize the overall distances the trucks must travel.

Please assume that each truck can only carry up to one cargo, each truck can only make up to one trip and that some trucks may not be used at all.

There are 2 csv files: cargo.csv and trucks.csv. Cargo.csv is a list of cargos we need to move and trucks.csv is a list of trucks and their home city.

## Main algorithm complexity:
The main algorithm is located on `FreightBroker` class, at `map_cargo_to_trucks()` method.
The space and time complexity is O(n²) considering `n` cargos and `m` trucks.

## Configuration:
Requires only numpy, so use you favorite virtual environment (or not)
```console
$ pip3 install -r requirements
```

Python version used for development tests: 
> Python 3.6

## Run tests:
To execute the tests, just:
```console
$ python3.6 tests.py
```

The description and expected results are described in each method. There are five tests:

Two unit tests:
* test_load_data_from_file
* test_sample_distance_euclidean_distance

Three integration tests:
* test_route_pickup_cargo_deliver_cargo
* test_route_pickup_cargo_deliver_cargo_and_truck_returns_to_home
* test_all_potential_distances_from_all_cargos

## Run main execution:
To execute:
```console
$ python3.6 main.py
```
In the `main.py` file, the implementation takes into account two possibilities:
1. After the delivery of the cargo, the truck returns to home and this cost is tracked.
2. The route tracking stops when the cargo is delivered.

At the end of each possibility, the results are printed like the model:
```python
"Cargo {cargo.id} will be carried by {truck.id} will travel: {distance}"
```

### Legal notice:
This source code is available under GPLv3.
