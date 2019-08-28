from helper import Models
import numpy


class Truck(Models):
    def __init__(self, element):
        super().__init__(*element)

    def euclidean_distance(self, origin, destination):
        return self.dist(origin.coord, destination.coord)

    def get_distance(self, truck, cargo, destination, truck_returns=False):
        pickup_cargo = self.euclidean_distance(truck, cargo)
        delivery_cargo = self.euclidean_distance(cargo, destination)
        back_truck = self.euclidean_distance(destination, truck) if truck_returns else 0
        return pickup_cargo + delivery_cargo + back_truck

    @staticmethod
    def dist(x, y):
        return numpy.sqrt(numpy.sum((x - y) ** 2))
