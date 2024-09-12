from tkinter import*
from tkinter import ttk
from train import Train
from PIL import Image,ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
import os


class Help:

    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Help Desk")

      
        # first header image  
        img=Image.open(r"C:\Users\Admin\OneDrive\Documents\PROJECT\PROJECT\Images_GUI\kim.jpg")
        img=img.resize((1366,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as label
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1366,height=130)

        # background image 
        bg1=Image.open(r"C:\Users\Admin\OneDrive\Documents\PROJECT\PROJECT\Images_GUI\bg.png")
        bg1=bg1.resize((1366,768),Image.ANTIALIAS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as label
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1366,height=768)


        #title section
        title_lb1 = Label(bg_img,text="HELP DESK",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1366,height=45)


        title_lb2 = Label(bg_img,text="email:nikhilrai01112003@gmail.com",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb2.place(x=50,y=100,width=1366,height=45)



if __name__ == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()

        