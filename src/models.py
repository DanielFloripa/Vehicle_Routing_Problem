import numpy


class Models(object):

    def __init__(self, name, city, state, origin_lat, origin_lng,
                 destination_city=None, destination_state=None, destination_lat=None, destination_lng=None):
        self.name = name
        self.city = city
        self.state = state
        self.id = f'{name.replace(" ", "_")}__{state}'
        self.lat = float(origin_lat)
        self.lng = float(origin_lng)
        self.destination_city = destination_city or city
        self.destination_state = destination_state or state
        self.destination_lat = float(destination_lat or origin_lat)
        self.destination_lng = float(destination_lng or origin_lng)
        self.origin = numpy.array((self.lat, self.lng))
        self.destination = numpy.array((self.destination_lat, self.destination_lng))

