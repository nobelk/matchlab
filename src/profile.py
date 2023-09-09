from abc import ABC, abstractmethod


class Profile(ABC):
    @abstractmethod
    def get_id(self) -> str:
        pass

    @abstractmethod
    def calculate_distance_between(self, other_profile: Profile) -> float:
        pass