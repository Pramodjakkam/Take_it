from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
# import tkinter.font __package__
import tkinter.font as font

frame=Tk()
frame.geometry('800x500')
frame.title("Travelling salesman problem")
frame.config(bg='white')
frame.maxsize(800,550)
frame.minsize(800,550)
img=Image.open("C:\\Users\\Gopal\\Desktop\\Map.png")
img=img.resize((500,300))
pic=ImageTk.PhotoImage(img)
v1=Label(image=pic)
v1.place(x=100,y=50)
# v1.place(x=100,y=35)
# lavle=Label(frame,text="Travelling salesman problem",font="")
# lavle.place(x=350,y=10)

boo=Label(frame,text="Travelling Salesman problem",bg="white",font=("Helvitika",20,'bold')).place(x=185,y=10)
m1=Menubutton(frame,text="select",font=("Helvitika",10,'bold'))
m1.grid()
m1.menu=Menu(m1,tearoff=0)
m1['menu']=m1.menu
option1=IntVar()
option2=IntVar()
option3=IntVar()
option4=IntVar()
option5=IntVar()
m1.menu.add_checkbutton(label='Jalandhar',variable=option1)
m1.menu.add_checkbutton(label='Ludhiana',variable=option2)
m1.menu.add_checkbutton(label='Chandigard',variable=option3)
m1.menu.add_checkbutton(label='Patiala',variable=option4)
m1.menu.add_checkbutton(label='Amrister',variable=option5)
choose=Label(text="Choose your starting point:",bg="white",font=("Helvitika",15,'bold')).place(x=90,y=400)
m1.place(x=365,y=405)
jil_jil=Button(frame,text="About the Developers",foreground="white",width=25,bg="black",font=("Helvitika",13,'bold')).place(x=250,y=450)
frame.mainloop()













































# from tkinter import *
# from tkinter import ttk 
# # from tkinter import *
# from PIL import ImageTk, Image  

# # import ttk from tkinter
# frame=Tk()
# frame.geometry('500x500')
# frame.minsize(200,300)
# frame.maxsize(500,500)
# # pic=PhotoImage(file="zero.png")
# # pic=PhotoImage(file="zero.png"/)
# # image1 = Image.open("C:\Users\Gopal\Downloads ")
# # p=PhotoImage(Image.open("zero.png"))
# my=ImageTk.PhotoImage(Image.open("C:\Users\Gopal\Desktop\test\python-f2"))
# label=Label(image=my)
# frame.mainloop()
# # from tkinter import *
# # from PIL import ImageTk, Image  

# # obj=Tk()
# # obj.geometry("800x900")
# # obj.minsize(200,300)
# # obj.maxsize(700,800)
# # l1=Label(text="Hi this is my Computer",
# #          font="arial 25 bold",
# #          bg="yellow",
# #          fg="green")
# # l1.pack(side="left",
# #         anchor="nw",
# #         fill=Y)
# # # pic=PhotoImage(file="zero.png")
# # image1 = Image.open("C:\Users\Gopal\Downloads ")
# # test = ImageTk.PhotoImage(image1)
# # # v1=Label(image=pic)
# # # v1.pack()

# # """image=Image.open("smile.jpeg")
# # photo=ImageTk.PhotoImage(image)
# # v2=Label(image=photo)
# # v2.pack()"""


# # obj.mainloop()













