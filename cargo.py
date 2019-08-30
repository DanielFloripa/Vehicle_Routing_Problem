from models import Models
import numpy as np


class Cargo(Models):
    def __init__(self, element):
        super().__init__(*element)
        self.truck_booking = None
        self.shortest_distance = np.Infinity
        self.all_potential_distances = []

