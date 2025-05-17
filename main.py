# this is the v3 version of the helper
# we made the backend first
# then we made the frontend

# Bibliotheken
import tkinter
import yaml
import csv
import logging
import os
import PIL

# get the correct path
absPathRoot = os.getcwd()
imgPath = os.path.join(absPathRoot, "images")
configPath = os.path.join(absPathRoot, "config")
#
logging.basicConfig(
    level=logging.INFO,
    filename="log.log",
    format="%(asctime)s:%(levelname)s:%(message)s",
)


# config loader
# load config from yaml file
def loadConfig(cfgLocation):
    with open("config.yml", "r") as f:
        pass


# predefiened loadout loader
def loadLoadout(loadoutLocation):
    pass

# image loader
def load_image(name, size):
    path = os.path.join(imgPath, name)
    img = PIL.Image.open(path).resize(size)
    logging.info(f"""Bild geladen: {path}""")
    return PIL.ImageTk.PhotoImage(img)


# Titelbildschirm
def titleScreen():
    pass # TODO: implement title screen using tkinter


def getEnemyType(mode):
    if mode == "CLI":
        pass
    elif mode == "GUI":
        pass
    else:
        logging.log(logging.ERROR, "Fehler: Ungültiger Modus ausgewählt, konfigutation nicht möglich")
    
def getDifficulty(mode):
    if mode == "CLI":
        pass
    elif mode == "GUI":
        pass
    else:
        logging.log(logging.ERROR, "Fehler: Ungültiger Modus ausgewählt, konfigutation nicht möglich")







if __name__ == "__main__":  # run only if executed as script
    titleScreen()
    enemyType = getEnemyType()
    difficulty = getDifficulty()
    # TODO: implement main function.
else:
    logging.log(logging.ERROR, "This module is not meant to be imported")
