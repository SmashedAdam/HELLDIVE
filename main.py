import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import time
import os

# Relative path
IMG_DIR = os.path.join(os.path.dirname(__file__), "images")


# Eine Funktion für das Laden von Bildern
def load_image(name, size):
    path = os.path.join(IMG_DIR, name)
    img = Image.open(path).resize(size)
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
        text="jetzt",
        font=("Arial", 14),
        command=enter,
        bg="black",
        fg="white",
    )
    start_btn.place(x=300, y=380, width=200, height=40)


# Mitte Interface
def show_main_ui():
    global enemy_type, difficulty, result_label, image_frame, loading_label, enemy_img_label

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

    def on_submit():
        enemy = enemy_type.get()
        try:
            diff = int(difficulty.get())
            if diff < 6:
                messagebox.showwarning("提示", "本辅助器不辅助1~5的残疾人")
                return
        except ValueError:
            messagebox.showerror("错误", "请输入有效数字")
            return

        loading_label.config(text="分析中，请稍候...")
        root.update()
        time.sleep(1)
        loading_label.config(text="")

        weapon_output = []
        weapon_imgs = []

        if enemy == "蟲族":
            weapon_output = ["盟友", "哨戒机枪", "轨道燃烧弹", "500kg炸弹"]
            weapon_imgs = ["friend.png", "gatling.png", "napalm.png", "bomb500.png"]
        elif enemy == "机器人":
            weapon_output = ["at炮台", "无后坐力炮", "轨道激光", "火箭炮台"]
            weapon_imgs = ["rocket.png", "recoiless.png", "laser.png", "huojian.png"]
        elif enemy == "光能族":
            weapon_output = ["飞鹰机枪", "无后坐力炮", "类星体", "轨道毒气"]
            weapon_imgs = ["hawk.png", "recoiless.png", "quasar.png", "gas.png"]
        else:
            result_label.config(text="未知敌人")
            return

        result_label.config(text="推荐武器：\n" + ", ".join(weapon_output))

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
    root.geometry("600x500")
    root.configure(bg="black")

    tk.Label(root, text="敌人类型：", bg="black", fg="white").pack(pady=(10, 0))
    enemy_type = ttk.Combobox(
        root, values=["蟲族", "机器人", "光能族"], state="readonly"
    )
    enemy_type.current(0)
    enemy_type.pack()
    enemy_type.bind("<<ComboboxSelected>>", update_enemy_img)

    enemy_img_label = tk.Label(root, bg="black")
    enemy_img_label.pack(pady=10)
    update_enemy_img()

    tk.Label(root, text="难度（6~10）：", bg="black", fg="white").pack()
    difficulty = tk.Entry(root)
    difficulty.pack()

    loading_label = tk.Label(root, text="", fg="yellow", bg="black")
    loading_label.pack()

    tk.Button(root, text="开始分析", command=on_submit, bg="green", fg="white").pack(
        pady=10
    )

    result_label = tk.Label(root, text="", bg="black", fg="cyan", font=("Arial", 12))
    result_label.pack(pady=10)

    image_frame = tk.Frame(root, bg="black")
    image_frame.pack(pady=5)

    tk.Button(
        root,
        text="非常不感谢你的使用，退出",
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
