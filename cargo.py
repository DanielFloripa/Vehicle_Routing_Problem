from helper import Models
import random
from math import sqrt
import numpy as np


class Cargo(Models):
    def __init__(self, element):
        super().__init__(*element)
        self.can_be_carried_by = None
        self.will_travel_shortest_distance = np.inf
        self.potential_distances = []

