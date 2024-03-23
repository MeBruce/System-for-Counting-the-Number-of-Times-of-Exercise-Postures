import tkinter as tk
import cv2
import requests
import tkinter.font as tkFont
from PIL import Image, ImageTk
from io import BytesIO
from tkinter import Tk, Frame
import torch
from torchvision.models import detection
import subprocess

class App:
    def __init__(self, root):
        # setting title
        root.title("The System Helps Count the Number of Exercise Postures")
        # โหลดรูปภาพโลโก้ที่คุณต้องการใช้
        logo_image = Image.open("image/iconsitup.png")
        # ปรับขนาดรูปภาพโลโก้ให้เหมาะสมกับไอคอน
        # ปรับขนาดเป็น 32x32 พิกเซล (ขนาดที่แนะนำ)
        logo_image = logo_image.resize((32, 32))
        # บันทึกรูปภาพโลโก้เป็นไฟล์ .ico
        logo_image.save("image/iconsitup.ico")
        # กำหนดไฟล์ไอคอนให้กับหน้าต่าง
        root.iconbitmap("image/iconsitup.ico")
        # setting window size
        root.geometry("1100x650")
        # Setting background color
        root.configure(bg="#76ABAE")

        # Creating the main frame
        main_frame = tk.Frame(root, width=1000, height=600,
                              borderwidth=2, relief="solid")
        main_frame.pack(side="top", pady=20)
        main_frame.configure(bg="#DFF5FF")

        # Creating the frame container
        frame_container = tk.Frame(root)
        frame_container.pack(side="bottom", pady=10)
        # กำหนดสีพื้นหลังของ frame_container
        frame_container.configure(bg="#76ABAE")


    # ดาวน์โหลดภาพจากเครื่อง
        # โหลดภาพ
        imagesitup = Image.open(
            "image/sit_up.png")
        # ปรับขนาดภาพให้เหมาะสมกับปุ่ม
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
        # situp_button["text"] = "sit up" #text ภายใน button
        situp_button.imagesitup = photositup  # เก็บ reference ของภาพ
        # situp_button.place(x=350,y=120,width=190,height=110)
        situp_button.place(in_=main_frame, x=170, y=150,
                          anchor='n', width=310, height=250)
        situp_button["command"] = self.situp_button_command

        imagepushup = Image.open(
            "image/push_up.png")
        # ปรับขนาดภาพให้เหมาะสมกับปุ่ม
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
        # pushup_button["text"] = "push up" #text ภายใน button
        pushup_button.imagepushup = photopushup  # เก็บ reference ของภาพ
        # pushup_button.place(x=580,y=120,width=190,height=110)
        pushup_button.place(in_=main_frame, x=500,y=150,
                          anchor='n', width=310, height=250)
        pushup_button["command"] = self.pushup_button_command

        imagesquat = Image.open(
            "image/squat.png")
        # ปรับขนาดภาพให้เหมาะสมกับปุ่ม
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
        # squat_button["text"] = "squat" #text ภายใน button
        squat_button.imagesquat = photosquat  # เก็บ reference ของภาพ
        # squat_button.place(x=810,y=120,width=190,height=110)
        squat_button.place(in_=main_frame, x=830, y=150,
                          anchor='n', width=310, height=250)
        squat_button["command"] = self.squat_button_command


    def situp_button_command(self):
        # เรียกไฟล์ count_situp.py ด้วย subprocess
        subprocess.run(["python", "count_situp.py"])
        print("count_situp")

    def pushup_button_command(self):
        # เรียกไฟล์ count_pushup.py ด้วย subprocess
        subprocess.run(["python", "count_pushup.py"])
        print("count_pushup")

    def squat_button_command(self):
        # เรียกไฟล์ count_squat.py ด้วย subprocess
        subprocess.run(["python", "count_squat.py"])
        print("count_squat")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
