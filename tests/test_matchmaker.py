from logging import Logger
import logging.config
import yaml

from src.matchmaker import Matchmaker

# logger
with open('log_config.yaml', 'r') as configFile:
    config = yaml.safe_load(configFile.read())
    logging.config.dictConfig(config)

logger: Logger = logging.getLogger(__name__)


def test_matchmaker():
    match_maker = Matchmaker(logger)