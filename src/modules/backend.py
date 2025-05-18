# Helldivers 2 Helper V3 - BACKEND


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


# Konfigurierung laden
def loadConfig(cfgLocation):
    with open(cfgLocation, "r", encoding="utf-8") as f:
        Konfigurationen = yaml.safe_load(f)
    return Konfigurationen


# Ausrustung von yaml laden
def loadLoadout(loadoutLocation):
    with open(loadoutLocation, "r", encoding="utf-8") as f:
        Ladeauswahl = yaml.safe_load(f)
    return Ladeauswahl


def giveAdvice(diff, faction, conf=loadConfig(), loadout=loadLoadout()):
    """Schwierigkeitsgrad und Fraktion eingeben, empfohlene Ausrüstung zurückgeben

    Args:
        diff (int): Schwierigkeitsgrad
        faction (str): feindliche Fraktion

    Returns:
       dict : ein Wörterbuch, das 4 Ausstattungsoptionen enthält
    """

    if diff > conf["minDiff"]:  # Schwerigkeit muss größer als minDiff
        if faction in conf["faction"]:
            advice = loadout[faction][f"{faction}1"]
        else:
            logging.log(logging.ERROR, "unbekannte Fraktion.")
            advice = None
    else:
        logging.log(logging.ERROR, "Schwierigkeitsgrad zu niedrig.")
        advice = None
    logging.log(logging.INFO, "Vorschläge genertiert.")
    return advice


if __name__ == "__main__":  # Wird nur ausgeführt, wenn es als Skript ausgeführt wird
    logging.log(logging.ERROR, "Dieses Modul ist nicht für den Import vorgesehen")
