import uuid
from logging import Logger
from profile import Profile
from typing import Tuple


class Matchmaker:
    def __init__(self, logger: Logger):
        self.logger = logger

    def match(self, profile: Tuple[Profile], match_size: int, func) -> Tuple[uuid]:
        pass