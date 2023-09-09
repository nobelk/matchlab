import random
import sys
import uuid
from profile import Profile
from logging import Logger
from typing import List


def random_matchmaking_strategy(logger: Logger, profiles: List[Profile]) -> List[uuid, uuid]:
    match = []
    if len(profiles) <= 2:
        match.append(profiles[0].id)
        match.append(profiles[1].id)
    else:
        uuid_index1 = random.randint(0, len(profiles) - 1)
        match.append(profiles[uuid_index1])
        profiles.delete(uuid_index1)
        uuid_index2 = random.randint(0, len(profiles) - 1)
        profiles.append(uuid_index2)

    return match


def min_distance_based_matchmaking_strategy(logger: Logger, main_profile: Profile, profiles: List[Profile]) -> List[str,str]:
    match = [main_profile.get_id()]
    min_distance_profile_id = str()
    min_distance = sys.maxsize
    for profile in profiles:
        catalogue[profile.get_id()] = main_profile.calculate_distance(profile)
    match = []

