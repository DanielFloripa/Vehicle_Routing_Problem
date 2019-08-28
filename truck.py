from helper import Models
import numpy


class Truck(Models):
    def __init__(self, element):
        super().__init__(*element)
        self.current_truck_location = self.origin

    def move_truck_to(self, cargo, destination, truck_returns=False):
        pickup_cargo = self.euclidean_distance(cargo)
        self.current_truck_location = cargo

        delivery_cargo = self.euclidean_distance(destination)
        self.current_truck_location = destination

        back_truck = self.euclidean_distance(self.origin) if truck_returns else 0
        self.current_truck_location = self.origin

        return pickup_cargo + delivery_cargo + back_truck

    def euclidean_distance(self, destination, new_origin=None):
        # origin = new_origin if new_origin is not None else self.origin
        return numpy.sqrt(numpy.sum((self.current_truck_location - destination) ** 2))
