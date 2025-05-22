from modules.backend import loadConfig, giveAdvice
import os

# den richtigen Pfad erhalten
absPathFile = os.path.abspath(__file__)
absPathRoot = os.path.dirname(absPathFile)
loadoutPath = os.path.join(absPathRoot, "config", "loadout.yml")
configPath = os.path.join(absPathRoot, "config", "config.yml")


config = loadConfig(configPath) # Konfiguration aus YAML-Datei laden


if __name__ != "__main__":  # Es muss im interaktiven Modus ausgeführt werden
    print("FEHLER: Dieses Programm muss direkt ausgeführt werden!")
else:
    if config["mode"] == "CLI":  # CLI Modus
        print("MODUS: CLI")
        diff = int(input("Bitte geben Sie die Schwerigkeit ein: "))  # Schwierigkeit
        print()
        factionSelect = int(
            input(
                "Bitte geben Sie die Fraktion ein [Terminiden(1)/Roboter(2)/Illuminierten(3)]: "  # einfachere Feindauswahl
            )
        )
        print()
        faction = config["faction"][factionSelect - 1]
        data = giveAdvice(diff, faction, configPath, loadoutPath)
        print("Empfohlene Waffen sind:")
        for v in data.values():
            print(f"   - {v}")  # besser visualle Wirkung

    elif config["mode"] == "GUI":
        print("MODUS: GUI")
        with open("./modules/alt.py") as file:
            exec(file.read())  # die unabhängige Version laufen
    else:
        print("Unbekannte Modus wählte")
