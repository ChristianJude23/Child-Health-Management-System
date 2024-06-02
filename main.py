import tkinter as tk

from tkinter import PhotoImage
from pathlib import Path
from PIL import Image, ImageTk

class LoginSignUp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1100x600")
        self.title("Child Health Management System")
        self.resizable(False, False)
        
        # Load Images
        self.OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = self.OUTPUT_PATH / "img"
        
        self.CreateVisuals()
        self.Canvas()
        self.CreateWidgets()
        
    def CreateVisuals(self):
        # Frame
        self.frm_sideBar = tk.Frame(self, width=300, height=600, bg="#EEF7FF")
        self.frm_Main = tk.Frame(self, width=800, height=600, bg="#CDE8E5")
        
        # Frame pos
        self.frm_sideBar.place(x=0, y=0)
        self.frm_Main.place(x=300, y=0)
        
        
    
    def CreateWidgets(self):
        # SideBar
        # SideBar Exit Button
        self.sideBar_btn_exit_img = PhotoImage(file=self.RelativeToAssets("Exit BTN.png"))
        self.sideBar_btn_exit = tk.Button(
            self.frm_sideBar,
            image=self.sideBar_btn_exit_img,
            borderwidth=0,
            cursor="hand2",
            relief="flat",
            highlightthickness=0,
            bg="#EEF7FF",
            command=lambda: print("BTN press")
            )
        self.sideBar_btn_exit.place(x=20, y=20)
        
        # SideBar Login Button
        self.sideBar_btn_login_img = PhotoImage(file=self.RelativeToAssets("BTN Log In.png"))
        self.sideBar_btn_login = tk.Button(
            self.frm_sideBar,
            image=self.sideBar_btn_login_img,
            borderwidth=0,
            cursor="hand2",
            command=lambda: print("BTN press")
        )
        self.sideBar_btn_login.place(x=50, y=230)
        
        # SideBar SignUp Button
        self.sideBar_btn_signup_img = PhotoImage(file=self.RelativeToAssets("BTN Sign Up.png"))
        self.sideBar_btn_signup = tk.Button(
            self.frm_sideBar,
            image=self.sideBar_btn_signup_img,
            borderwidth=0,
            cursor="hand2",
            command=lambda: print("BTN press")
        )
        self.sideBar_btn_signup.place(x=50, y=300)
        
        # SideBar CopyRight
        lbl_copyright = tk.Label(self.frm_sideBar, text="©2024", font=("Inter", 16, "bold"), bg="#EEF7FF").place(x=110, y=570)
    
    def Canvas(self):
        # SideBar
        self.cnv_sideBar = tk.Canvas(self.frm_sideBar, bg="#EEF7FF", width=300, height=600)
        self.cnv_sideBar.place(x=0, y=0)
        
        # SideBar Top Image
        img_path = self.RelativeToAssets("SideBar TopImage.png")
        image = Image.open(img_path)
        resized_image = image.resize((120, 90))
        self.sideBar_Top_img = ImageTk.PhotoImage(resized_image)
        self.cnv_sideBar.create_image(85, 50, anchor='nw', image=self.sideBar_Top_img)
        
    
    def RelativeToAssets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)


if __name__ == "__main__":
    win = LoginSignUp()
    win.mainloop()