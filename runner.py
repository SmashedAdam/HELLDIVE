import yaml

def loadLoadout(loadoutLocation):
    with open(loadoutLocation, "r", encoding="utf-8") as f:
        Ladeauswahl = yaml.safe_load(f)
    return Ladeauswahl



print(loadLoadout("./config/loadout.yml"))