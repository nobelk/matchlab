import math
from profile import Profile


class DefaultGameProfile(Profile):
    def __init__(self, id: str, strength: float, speed: float):
        self.id = id
        self.strength = strength
        self.speed = speed

    def get_id(self):
        return self.id

    def calculate_distance_between(self, other: Profile):
        sum = (self.strength - other.strength) ^ 2 + (self.speed - other.speed) ^ 2
        return math.sqrt(sum)

    def __eq__(self, other):
        return self.id == other.get_id()
