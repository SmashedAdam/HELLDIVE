# this is the v3 version of the helper
# we made the backend first
# he is the backend

# then we made the frontend

# Bibliotheken

import yaml
import logging
import os


# get the correct path
absPathRoot = os.getcwd()
loadoutPath = os.path.join(absPathRoot, "loadout")
configPath = os.path.join(absPathRoot, "config")


# config logging
logging.basicConfig(
    level=logging.INFO,
    filename="log.log",
    format="%(asctime)s:%(levelname)s:%(message)s",
    encoding="utf-8",
)


# config loader
# Konfigurierung laden
def loadConfig(cfgLocation):
    with open(cfgLocation, "r", encoding="utf-8") as f:
        Konfigurationen = yaml.safe_load(f)
    return Konfigurationen


# load pre-defined loadout
def loadLoadout(loadoutLocation):
    with open(loadoutLocation, "r", encoding="utf-8") as f:
        Ladeauswahl = yaml.safe_load(f)
    return Ladeauswahl


if __name__ == "__main__":  # run only if executed as script
    conf = loadConfig("./config/config.yml")
    loadout = loadLoadout("./config/loadout.yml")
    # asks user for selected difficulty

else:
    logging.log(logging.ERROR, "This module is not meant to be imported")
