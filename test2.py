import tkinter as tk
from PIL import Image, ImageTk

class App:
    def __init__(self, root):
        root.title("เปลี่ยนโลโก้")
        root.geometry("400x300")
        
        # โหลดรูปภาพโลโก้
        logo_image = Image.open("F:\\FINAL PROJECT\\Project2\\UI\\squat.jpg")
        
        # ปรับขนาดรูปภาพ
        logo_image = logo_image.resize((200, 200))
        
        # แปลงรูปภาพเป็นรูปแบบที่ tkinter รองรับ
        self.logo_photo = ImageTk.PhotoImage(logo_image)
        
        # สร้าง Label เพื่อแสดงโลโก้
        self.logo_label = tk.Label(root, image=self.logo_photo)
        self.logo_label.pack()
        
        # สร้างปุ่มเพื่อเปลี่ยนโลโก้
        change_button = tk.Button(root, text="เปลี่ยนโลโก้", command=self.change_logo)
        change_button.pack()
    
    def change_logo(self):
        # โหลดรูปภาพใหม่
        new_logo_image = Image.open("new_logo.png")
        
        # ปรับขนาดรูปภาพ
        new_logo_image = new_logo_image.resize((200, 200))
        
        # แปลงรูปภาพใหม่เป็นรูปแบบที่ tkinter รองรับ
        self.logo_photo = ImageTk.PhotoImage(new_logo_image)
        
        # อัปเดตรูปภาพใน Label
        self.logo_label.config(image=self.logo_photo)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
