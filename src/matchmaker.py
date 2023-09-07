import uuid
from logging import Logger
from typing import List, Tuple


class Matchmaker:
    def __init__(self, logger: Logger):
        self.logger = logger

    def match(self, profile: Tuple, match_size: int, func) -> Tuple[uuid]:
        pass