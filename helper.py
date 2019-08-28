import csv
import numpy


class Models(object):

    def __init__(self, name, city, state, origin_lat, origin_lng,
                 destination_city=None, destination_state=None, destination_lat=None, destination_lng=None):
        self.name = name
        self.city = city
        self.state = state
        self.uniq_id = f'{name.replace(" ", "_")}__{state}'
        self.lat = float(origin_lat)
        self.lng = float(origin_lng)
        self.destination_city = destination_city or city
        self.destination_state = destination_state or state
        self.destination_lat = float(destination_lat or origin_lat)
        self.destination_lng = float(destination_lng or origin_lng)
        self.origin = Coordinates(self.lat, self.lng)
        self.destination = Coordinates(self.destination_lat, self.destination_lng)


class Coordinates(object):
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
