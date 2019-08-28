import csv
import numpy


class Models(object):

    def __init__(self, name, city, state, origin_lat, origin_lng, destination_city=None, destination_state=None, destination_lat=None, destination_lng=None):
        self.name = name
        self.city = city
        self.state = state
        self.uniq_id = f'{name.replace(" ", "_")}__{city.replace(" ", "_")}__{state}'
        self.lat = float(origin_lat)
        self.lng = float(origin_lng)
        self.destination_city = destination_city or city
        self.destination_state = destination_state or state
        self.destination_lat = float(destination_lat or origin_lat)
        self.destination_lng = float(destination_lng or origin_lng)
        self.origin = Coordinate(self.lat, self.lng)
        self.destination = Coordinate(self.destination_lat, self.destination_lng)

    def euclidean_distance(self, origin, destination):
        return self.dist(origin.coord, destination.coord)

    def get_distance(self, truck, cargo, destination):
        pickup_cargo = self.euclidean_distance(truck, cargo)
        delivery_cargo = self.euclidean_distance(cargo, destination)
        back_truck = self.euclidean_distance(destination, truck)
        return pickup_cargo + delivery_cargo + back_truck

    @staticmethod
    def dist(x, y):
        return numpy.sqrt(numpy.sum((x - y) ** 2))


class Coordinate(object):
    def __init__(self, lat, lng):
        self.lat = float(lat)
        self.lng = float(lng)
        self.coord = numpy.array((self.lat, self.lng))

    def get_coordinates(self):
        return [self.lat, self.lng]


class LoadData(object):
    def __init__(self, class_type, file):
        self.csv_file = file
        self.list_from_file = self.__load_file()
        self.list = self.object_creator(class_type)

    def object_creator(self, class_type):
        return [class_type(obj) for obj in self.list_from_file[1:]]

    def __load_file(self):
        with open(self.csv_file, "r") as fp:
            load = csv.reader(fp)
            return [line for line in load]


class UnitTest(object):

    def __init__(self, file):
        self.file = file
        self.coordinates = [0,0]
