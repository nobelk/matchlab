import logging.config
from logging import Logger
from src import matchmaker
import yaml

# logger
with open('log_config.yaml', 'r') as configFile:
    config = yaml.safe_load(configFile.read())
    logging.config.dictConfig(config)

logger: Logger = logging.getLogger(__name__)


def main():
    match_maker = Matchmaker(logger)


if __name__ == '__main__':
    main()
