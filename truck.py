from helper import Models
import random
from math import sqrt
import numpy as np


class Truck(Models):
    def __init__(self, element):
        super().__init__(*element)
        self.pickup = None
        self.distance = -1
