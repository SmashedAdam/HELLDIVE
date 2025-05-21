from modules.backend import loadConfig, giveAdvice
import os

# get the correct path
absPathFile = os.path.abspath(__file__)
absPathRoot = os.path.dirname(absPathFile)
loadoutPath = os.path.join(absPathRoot, "config", "loadout.yml")
configPath = os.path.join(absPathRoot, "config", "config.yml")


config = loadConfig(configPath)


if __name__ != "__main__":
    print("FEHLER: Dieses Programm muss direkt ausgeführt werden!")
else:
    if config["mode"] == "CLI":
        print("MODUS: CLI")
        diff = int(input("Bitte geben Sie die Schwerigkeit ein: "))
        print()
        factionSelect = int(
            input(
                "Bitte geben Sie die Fraktion ein [Terminiden(1)/Roboter(2)/Illuminierten(3)]: "
            )
        )
        print()
        faction = config["faction"][factionSelect - 1]
        data = giveAdvice(diff, faction, configPath, loadoutPath)
        print("Empfohlene Waffen sind:")
        for v in data.values():
            print(f"   - {v}")

    elif config["mode"] == "GUI":
        print("MODUS: GUI")
        with open("./modules/legacy.py") as file:
            exec(file.read())
    else:
        print("Unbekannte Modus wählte")
