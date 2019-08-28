# Assessment based in Vehicle Routing Problem (VRP)

## Problem description:
Given a list of trucks and their current locations and a list of cargos and their pickup and delivery locations, find the optimal mapping of trucks to cargos to minimize the overall distances the trucks must travel.

Please assume that each truck can only carry up to one cargo, each truck can only make up to one trip and that some trucks may not be used at all.

There are 2 csv files: cargo.csv and trucks.csv. Cargo.csv is a list of cargos we need to move and trucks.csv is a list of trucks and their home city.

## Configuration:
Requires only numpy, so use you favorite virtual environment (or not)
> $ pip install -r requirements

Version used for tests: 
> Python 3.6