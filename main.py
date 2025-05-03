import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import time
import os

# TODO: implement V2: logging + config
import logging
import yaml


# logging:
logging.basicConfig(
    filename="./log.log",
    level=logging.INFO,
    format="%(asctime)s:%(levelname)s:%(message)s",
)
logging.info("Programm gestartet")


# Relative path
IMG_DIR = os.path.join(os.path.dirname(__file__), "images")


# Eine Funktion für das Laden von Bildern
def load_image(name, size):
    path = os.path.join(IMG_DIR, name)
    img = Image.open(path).resize(size)
    logging.info(f"""Bild geladen: {path}""")
    return ImageTk.PhotoImage(img)


# Titelbildschirm
def show_start_screen():
    start = tk.Toplevel()
    start.title("Helldivers 2-Ausrüstungshelfer")
    start.geometry("800x450")
    start.resizable(False, False)

    bg = load_image("start_bg.jpeg", (800, 450))
    panel = tk.Label(start, image=bg)
    panel.image = bg
    panel.pack()

    def enter():
        start.destroy()
        show_main_ui()

    start_btn = tk.Button(
        start,
        text="Auswahlassistent starten",
        font=("Arial", 14),
        command=enter,
        bg="black",
        fg="white",
    )
    start_btn.place(x=280, y=380, width=220, height=40)
    logging.info("Start-UI zeigten")


# Mitte Interface
def show_main_ui():
    global enemy_type, difficulty, result_label, image_frame, loading_label, enemy_img_label
    logging.info("Main-UI wird gezeigt")

    def update_enemy_img(event=None):
        sel = enemy_type.get()
        if sel == "Terminiden":
            img = load_image("zerg.png", (150, 150))
        elif sel == "Roboter":
            img = load_image("robot.png", (150, 150))
        elif sel == "Illuminierten":
            img = load_image("energy.png", (150, 150))
        else:
            return
        enemy_img_label.config(image=img)
        enemy_img_label.image = img
        logging.info("Feind auswählten")

    def on_submit():
        enemy = enemy_type.get()
        try:
            diff = int(difficulty.get())
            if diff < 6:
                logging.warning("Schwierigkeitsgrad zu niedrig")
                messagebox.showwarning(
                    title="WARNUNG",
                    message="Der Schwierigkeitsgrad ist zu niedrig, keine passenden Vorschläge.",
                )
                return
            elif diff > 10:
                logging.warning("Schwierigkeitsgrad zu hoch")
                messagebox.showwarning(
                    title="WARNUNG",
                    message="Der Schwierigkeitsgrad ist nicht verfugbar in dem Spiel.",
                )
                return
        except ValueError:
            logging.error("FEHLER: ungültige Nummer")
            messagebox.showerror(title="FEHLER", message="FEHLER: ungültige Nummer")
            return

        loading_label.config(text="Analyse läuft...")
        root.update()
        time.sleep(1)
        loading_label.config(text="")

        weapon_output = []
        weapon_imgs = []

        if enemy == "Terminiden":
            weapon_output = [
                "STALWART",
                "MG-Geschütz",
                "Napalm-Orbitalsperrfeuer",
                "ADLER-500KG-Bombe",
            ]
            weapon_imgs = [
                "stalwart.png",
                "Maschinengewehr-Geschütz.png",
                "napalm.png",
                "bomb500.png",
            ]
        elif enemy == "Roboter":
            weapon_output = [
                "Panzerabwehrstellung",
                "rückstossfreies Gewehr",
                "Orbital-Laser",
                "Raketengeschütz",
            ]
            weapon_imgs = [
                "ATEmplacement.png",
                "recoiless.png",
                "OrbitalLaser.png",
                "RKTSentry.png",
            ]
        elif enemy == "Illuminierten":
            weapon_output = [
                "Adler-Tieffliegerangriff",
                "rückstossfreies Gewehr",
                "Quasarkanone",
                "Orbital-Gasangriff",
            ]
            weapon_imgs = [
                "Adler-Tieffliegerangriff.png",
                "recoiless.png",
                "quasar.png",
                "gas.png",
            ]
        else:
            result_label.config(text="unbekannter Feind")
            logging.error("unbekannter Feind")
            return

        result_label.config(text="Empfohlene Waffen:\n" + ", ".join(weapon_output))

        for widget in image_frame.winfo_children():
            widget.destroy()

        for img_name in weapon_imgs:
            icon = load_image(img_name, (64, 64))
            lbl = tk.Label(image_frame, image=icon, bg="black")
            lbl.image = icon
            lbl.pack(side=tk.LEFT, padx=5)

    # mittefenster Einstellung
    root.deiconify()
    root.title("helldive2waffenauswahlhilfsprogramm")
    root.geometry("600x600")
    root.configure(bg="black")

    tk.Label(root, text="feindetyp:", bg="black", fg="white").pack(pady=(10, 0))
    enemy_type = ttk.Combobox(
        root, values=["Terminiden", "Roboter", "Illuminierten"], state="readonly"
    )
    enemy_type.current(0)
    enemy_type.pack()
    enemy_type.bind("<<ComboboxSelected>>", update_enemy_img)

    enemy_img_label = tk.Label(root, bg="black")
    enemy_img_label.pack(pady=10)
    update_enemy_img()

    tk.Label(root, text="Schwierigkeit(6~10):", bg="black", fg="white").pack()
    difficulty = tk.Entry(root)
    difficulty.pack()

    loading_label = tk.Label(root, text="", fg="yellow", bg="black")
    loading_label.pack()

    tk.Button(
        root, text="jetzt analysieren", command=on_submit, bg="green", fg="white"
    ).pack(pady=10)

    result_label = tk.Label(root, text="", bg="black", fg="cyan", font=("Arial", 12))
    result_label.pack(pady=10)

    image_frame = tk.Frame(root, bg="black")
    image_frame.pack(pady=5)

    tk.Button(
        root,
        text="Schließen",
        command=root.destroy,
        bg="red",
        fg="white",
    ).pack(pady=10)


# angang fur start program
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    show_start_screen()
    root.mainloop()
