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
        
        # Get Image folder
        self.OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = self.OUTPUT_PATH / "assets/LoginSignUpImg"
        
        self.CreateFrame()
        self.Canvas()
        self.CreateWidgets()
        
    def CreateFrame(self):
        # Frame
        self.frm_sideBar = tk.Frame(self, width=300, height=600, bg="#EEF7FF")
        self.frm_MainHome = tk.Frame(self, width=800, height=600, bg="#CDE8E5")
        self.frm_MainLogin = tk.Frame(self, width=800, height=600, bg="#CDE8E5")
        self.frm_MainSigUp = tk.Frame(self, width=800, height=600, bg="#CDE8E5")
        
        # Frame pos
        self.frm_sideBar.place(x=0, y=0)
        self.frm_MainHome.place(x=300, y=0)
            
    def CreateWidgets(self):
        # -------------------------------------------------- SideBar ---------------------------------------
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
            command=self.LoginFrameWidgets
        )
        self.sideBar_btn_login.place(x=50, y=230)
        
        # SideBar SignUp Button
        self.sideBar_btn_signup_img = PhotoImage(file=self.RelativeToAssets("BTN Sign Up.png"))
        self.sideBar_btn_signup = tk.Button(
            self.frm_sideBar,
            image=self.sideBar_btn_signup_img,
            borderwidth=0,
            cursor="hand2",
            command=self.SignUpFrameWdgets
        )
        self.sideBar_btn_signup.place(x=50, y=290)
        
        # SideBar CopyRight
        lbl_copyright = tk.Label(self.frm_sideBar, text="©2024", font=("Inter", 16, "bold"), bg="#EEF7FF").place(x=110, y=570)


        # ----------------------------------------- Main Frame ------------------------------------------------
        # MainFrame Title
        lbl_title = tk.Label(self.frm_MainHome, text="Child Health Management System", font=("Inter", 24, "bold"), bg="#CDE8E5").place(x=130, y=20)
        
           
    def Canvas(self):
        # ------------------------------------------------ SideBar ---------------------------------------------------------
        # Canvas Declaration
        self.cnv_sideBar = tk.Canvas(self.frm_sideBar, bg="#EEF7FF", width=300, height=600)
        self.cnv_sideBar.place(x=0, y=0)
        
        # SideBar Top Image
        img_path = self.RelativeToAssets("SideBar TopImage.png")
        image = Image.open(img_path)
        resized_image = image.resize((120, 90))
        self.sideBar_Top_img = ImageTk.PhotoImage(resized_image)
        self.cnv_sideBar.create_image(85, 50, anchor='nw', image=self.sideBar_Top_img)
        
        # ------------------------------------------------ Main Frame -----------------------------------------------------
        # Canvas Declaration
        self.cnv_mainFrame = tk.Canvas(self.frm_MainHome, bg="#CDE8E5", width=800, height=600)
        self.cnv_mainFrame.place(x=0, y=0)
        
        # MainFrame Image
        img_path = self.RelativeToAssets("heartbeat 1.png")
        image = Image.open(img_path)
        resized_image = image.resize((400, 400))
        self.mainFrame_img = ImageTk.PhotoImage(resized_image)
        self.cnv_mainFrame.create_image(180, 120, anchor="nw", image=self.mainFrame_img)
    
    def LoginFrameWidgets(self):
        # Frames
        self.frm_MainHome.place_forget()
        self.frm_MainSigUp.place_forget()
        self.frm_loginForm = tk.Frame(self.frm_MainLogin, width=450, height=350, bg="#CDE8E5")
        
        self.frm_loginForm.place(x=160, y=130)
        self.frm_MainLogin.place(x=300, y=0)
        
        # Title
        lbl_title = tk.Label(self.frm_MainLogin, text="Child Health Management System", font=("Inter", 24, "bold"), bg="#CDE8E5").place(x=130, y=20)
        
        
        # Frame BG Image
        img_path = self.RelativeToAssets("LoginFrame.png")
        image = Image.open(img_path)
        resized_image = image.resize((430, 330))
        self.frame_loginForm_img = ImageTk.PhotoImage(resized_image)

        lbl_img = tk.Label(self.frm_loginForm, image=self.frame_loginForm_img, bg="#CDE8E5")
        lbl_img.place(x=10, y=10)
        
        # Login Form Widgets
        lbl_usernameLogin = tk.Label(self.frm_loginForm, text="Username", font=("Inter", 14), bg="#EEF7FF").place(x=50, y=40)
        lbl_passwordLogin = tk.Label(self.frm_loginForm, text="Password", font=("Inter", 14), bg="#EEF7FF").place(x=50, y=130)
        
        self.ent_usernameLogin = tk.Entry(self.frm_loginForm, bd=1, highlightthickness=0, font=("Inter", 14)) 
        self.ent_passwordLogin = tk.Entry(self.frm_loginForm, bd=1, highlightthickness=0, font=("Inter", 14), show="*")
             
        self.ent_usernameLogin.place(x=50, y=70, width=350, height=30)
        self.ent_passwordLogin.place(x=50, y=160, width=350, height=30)
        
        self.btn_loginForm_img = PhotoImage(file=self.RelativeToAssets("BTN Log In Form.png"))
        self.btn_loginForm = tk.Button(
            self.frm_loginForm,
            image=self.btn_loginForm_img,
            borderwidth=0,
            cursor="hand2",
            command=lambda: print("BTN Press")
        )
        self.btn_loginForm.place(x=120, y=230)

    def SignUpFrameWdgets(self):
        self.frm_MainHome.place_forget()
        self.frm_MainLogin.place_forget()
        self.frm_MainSigUp.place(x=300, y=0)
        
        # Title
        lbl_title = tk.Label(self.frm_MainSigUp, text="Child Health Management System", font=("Inter", 24, "bold"), bg="#CDE8E5").place(x=130, y=20)
    
    
    # Image path finding
    def RelativeToAssets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)
    
    
if __name__ == "__main__":
    win = LoginSignUp()
    win.mainloop()