import tkinter as tk
import tkinter.font as tkFont
from PIL import Image, ImageTk
import subprocess

class App:
    def __init__(self, root):
        root.title("The System Helps Count the Number of Exercise Postures")
        logo_image = Image.open("image/iconsitup.png")
        logo_image = logo_image.resize((32, 32))
        logo_image.save("image/iconsitup.ico")
        root.iconbitmap("image/iconsitup.ico")
        root.geometry("1100x650")
        root.configure(bg="#76ABAE")

        main_frame = tk.Frame(root, width=1000, height=600,
                              borderwidth=2, relief="solid")
        main_frame.pack(side="top", pady=20)
        main_frame.configure(bg="#DFF5FF")

        frame_container = tk.Frame(root)
        frame_container.pack(side="bottom", pady=10)
        frame_container.configure(bg="#76ABAE")


        imagesitup = Image.open(
            "image/sit_up.png")
        imagesitup = imagesitup.resize((150, 150))
        photositup = ImageTk.PhotoImage(imagesitup)

        situp_button = tk.Button(root, image=photositup)
        situp_button_text = tk.Label(root, text="คลิกเพื่อทำการ Sit Up",font=("Helvetica", 20))
        situp_button_text.place(in_=main_frame, x=50, y=450)
        situp_button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=15)
        situp_button["font"] = ft
        situp_button["fg"] = "#000000"
        situp_button["justify"] = "center"
        situp_button.imagesitup = photositup  
        situp_button.place(in_=main_frame, x=170, y=150,
                          anchor='n', width=310, height=250)
        situp_button["command"] = self.situp_button_command

        imagepushup = Image.open(
            "image/push_up.png")
        imagepushup = imagepushup.resize((190, 190))
        photopushup = ImageTk.PhotoImage(imagepushup)

        pushup_button = tk.Button(root, image=photopushup)
        pushup_button_text = tk.Label(root, text="คลิกเพื่อทำการ Push Up",font=("Helvetica", 20))
        pushup_button_text.place(in_=main_frame, x=360, y=450)
        pushup_button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=15)
        pushup_button["font"] = ft
        pushup_button["fg"] = "#000000"
        pushup_button["justify"] = "center"
        pushup_button.imagepushup = photopushup
        pushup_button.place(in_=main_frame, x=500,y=150,
                          anchor='n', width=310, height=250)
        pushup_button["command"] = self.pushup_button_command

        imagesquat = Image.open(
            "image/squat.png")
        imagesquat = imagesquat.resize((110, 110))
        photosquat = ImageTk.PhotoImage(imagesquat)

        squat_button = tk.Button(root, image=photosquat)
        squat_button_text = tk.Label(root, text="คลิกเพื่อทำการ Squat",font=("Helvetica", 20))
        squat_button_text.place(in_=main_frame, x=700, y=450)
        squat_button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=15)
        squat_button["font"] = ft
        squat_button["fg"] = "#000000"
        squat_button["justify"] = "center"
        squat_button.imagesquat = photosquat 
        squat_button.place(in_=main_frame, x=830, y=150,
                          anchor='n', width=310, height=250)
        squat_button["command"] = self.squat_button_command


    def situp_button_command(self):
        subprocess.run(["python", "count_situp.py"])
        print("count_situp")

    def pushup_button_command(self):
        subprocess.run(["python", "count_pushup.py"])
        print("count_pushup")

    def squat_button_command(self):
        subprocess.run(["python", "count_squat.py"])
        print("count_squat")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
