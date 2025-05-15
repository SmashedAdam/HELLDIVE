# this is the v3 version of the helper
# we made the backend first
# then we made the frontend

# Bibliotheken
import yaml
import csv
import logging

logging.basicConfig(level=logging.INFO, filename="log.log")


# config loader
# load config from yaml file
def loadConfig(cfgLocation):
    pass

# predefiened loadout loader
def loadLoadout(loadoutLocation):
    pass

if __name__ == "__main__": # run only if executed as script
    pass
else:
    logging.log(logging.ERROR, "This module is not meant to be imported")
    