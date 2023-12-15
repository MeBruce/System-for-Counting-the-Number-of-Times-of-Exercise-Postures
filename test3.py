import tkinter as tk
import requests
import tkinter.font as tkFont
from PIL import Image, ImageTk
from io import BytesIO

class App:
    def __init__(self, root):
        #setting title
        root.title("The System Helps Count the Number of Exercise Postures")
        
        #setting window size
        root.geometry("1600x900")
       
        # สร้างกรอบหลัก
        main_frame = tk.Frame(root, width=1000, height=600, borderwidth=2, relief="solid")
        main_frame.pack(side="top", pady=20)

        # สร้างกรอบเพิ่ม
        frame_container = tk.Frame(root)
        frame_container.pack(side="bottom", pady=10)

        # สร้างกรอบภายใน frame_container
        frame1 = tk.Frame(frame_container, width=400, height=300, borderwidth=2, relief="solid")
        frame1.pack(side="left", padx=20)
        frame2 = tk.Frame(frame_container, width=400, height=300, borderwidth=2, relief="solid")
        frame2.pack(side="left", padx=20)
        frame3 = tk.Frame(frame_container, width=400, height=300, borderwidth=2, relief="solid")
        frame3.pack(side="left", padx=20)

        # ดาวน์โหลดภาพจากเว็บไซต์
        response = requests.get("https://www.topendsports.com/fitness/images/sit-up-girl-pixa.jpg")
        image_data = response.content
       
        # โหลดภาพ
        image = Image.open(BytesIO(image_data))
        image = image.resize((150, 40))  # ปรับขนาดภาพให้เหมาะสมกับปุ่ม
        photo = ImageTk.PhotoImage(image)

        GButton_872 = tk.Button(frame1, image=photo)
        GButton_872["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=15)
        GButton_872["font"] = ft
        GButton_872["fg"] = "#000000"
        GButton_872["justify"] = "center"
        GButton_872["text"] = "sit up"
        GButton_872.place(x=350,y=120,width=190,height=110)
        GButton_872["command"] = self.GButton_872_command

    def GButton_872_command(self):
        print("command")

# รันโปรแกรมหลัก
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()