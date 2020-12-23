from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
 
 
 
class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Python Tkinter Dialog Widget")
        self.minsize(640, 400)
        self.wm_iconbitmap('icon.ico')
 
        self.labelFrame = ttk.LabelFrame(self, text = "Open File")
        self.labelFrame.grid(column = 0, row = 1, padx = 20, pady = 20)
 
        self.button()
 
 
 
    def button(self):
        self.button = ttk.Button(self.labelFrame, text = "Browse A File",command = self.fileDialog)
        self.button.grid(column = 1, row = 1)
 
 
    def fileDialog(self):
 
        self.filename = filedialog.askopenfilename(initialdir =  "S:/", title = "Select A File", filetype =
        (("jpeg files","*.jpg"),("all files","*.*")) )
        self.label = ttk.Label(self.labelFrame, text = "")
        self.label.grid(column = 1, row = 2)
        self.label.configure(text = self.filename)
        messagebox.showerror("Error",self.filename)
 
 
 
 
 
root = Root()
root.mainloop()



from tkinter import*
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
import pymysql
class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Graphical Authentication System")
        self.root.geometry("1366x768+0+0")

        title=Label(self.root,text="Graphical Authentication System",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="grey",fg="white",)
        title.pack(side=TOP,fill=X)

        #=========All Variables===========================

        self.Roll_No_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.gender_var=StringVar()
        self.contact_var=StringVar()
        self.dob_var=StringVar()
        self.search_by=StringVar()
        self.search_txt=StringVar()
        self.filename=StringVar()
        self.Detail1_Frame=Frame()
         #=========Manage Frame===========================
        try:
            Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="LightBlue1")
            #Manage_Frame.place(x=20,y=100,width=450,height=580)
            Manage_Frame.pack(side=TOP,fill=X)
            reg_btn=Button(Manage_Frame,text="Register",width=0,font=("times new roman",20,"bold")).grid(row=0,column=0,padx=1,pady=0)
            #Button(Manage_Frame,text="Login",width=10).grid(row=0,column=1,padx=10,pady=10)
            log_btn=Button(Manage_Frame,text="Login",width=0,font=("times new roman",20,"bold")).grid(row=0,column=1,padx=1,pady=0)

            #=========Manage1 Frame===========================

            Manage1_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="lightgreen")
            Manage1_Frame.place(x=20,y=160,width=450,height=520)

            m_title=Label(Manage1_Frame,text="Registration",bg="lightgreen",fg="black",font=("times new roman",30,"bold"))
            m_title.grid(row=0,columnspan=2,padx=110,pady=15)

            lbl_email=Label(Manage1_Frame,text="Email Availability",bg="lightgreen",fg="black",font=("times new roman",18,"bold"))
            lbl_email.grid(row=1,column=0,pady=10,padx=20,sticky="w")

            txt_email=Entry(Manage1_Frame,textvariable=self.Roll_No_var,width=30,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
            txt_email.grid(row=2,column=0,pady=0,padx=20,sticky="w")

            ver_btn=Button(Manage1_Frame,text="Verify",font=("times new roman",15,"bold")).grid(row=3,column=0,padx=80,pady=10,sticky="w")

            pro_btn=Button(Manage1_Frame,text="Proceed",font=("times new roman",15,"bold")).grid(row=3,column=0,padx=190,pady=10)

            lbl_image=Label(Manage1_Frame,text="Upload Picture",bg="lightgreen",fg="black",font=("times new roman",18,"bold"))
            lbl_image.grid(row=4,column=0,pady=10,padx=20,sticky="w")

            load_btn=Button(Manage1_Frame,text="Load Picture",command=self.fileDialog,font=("times new roman",15,"bold")).grid(row=4,column=0,padx=190,pady=10)

            #=========Detail Frame===========================

            Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="lightgreen")
            Detail_Frame.place(x=500,y=160,width=830,height=520)

            m_title1=Label(Detail_Frame,text="",bg="lightgreen")
            m_title1.grid(row=0,column=0,padx=110,pady=15)

            m_title=Label(Detail_Frame,text="Image",bg="lightgreen",fg="black",font=("times new roman",30,"bold"))
            m_title.grid(row=0,column=1,padx=110,pady=15)

            #=========Detail1 Frame===========================

            self.Detail1_Frame=Frame(Detail_Frame,bd=0,relief=RIDGE,bg="crimson")
            self.Detail1_Frame.place(x=80,y=80,width=665,height=410)
            #print("hi")
            self.Detail1_Frame.bind("<Button-1>",self.printcoords)
        except Exception as e:
            print(e)
    #=========Detail1 Frame image function===========================
    
    def fileDialog(self): 
        self.filename = filedialog.askopenfilename(initialdir =  "S:/", title = "Select A File", filetype =
        (("jpeg files","*.jpg"),("all files","*.*")) )
        if(self.filename!=""):
            load = Image.open(self.filename)
            render = ImageTk.PhotoImage(load)
            img = Label(self.Detail1_Frame, image=render)
            img.image = render
            img.place(x=3, y=3 ,width=658, height=404)
            #self.Detail1_Frame.config(scrollregion=self.Detail1_Frame.bbox(ALL))
        #function to be called when mouse is clicked
    def printcoords(self,event):
        #outputting x and y coords to console
        #print (event.x,event.y)
        g=str(event.x)
        f=str(event.y)
        g=g+" "+f
        messagebox.showerror("Error",g)
        #mouseclick event
           

root=Tk()
obj =Student(root)
root.mainloop()


from tkinter import*
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
import pymysql
class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Graphical Authentication System")
        self.root.geometry("1366x768+0+0")

        title=Label(self.root,text="Graphical Authentication System",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="grey",fg="white",)
        title.pack(side=TOP,fill=X)

        #=========All Variables===========================

        self.Roll_No_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.gender_var=StringVar()
        self.contact_var=StringVar()
        self.dob_var=StringVar()
        self.search_by=StringVar()
        self.search_txt=StringVar()
        self.filename=StringVar()
        self.Detail1_Frame=Frame()
        self.img=Label()
         
        try:
            #=========Manage Frame===========================
            Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="LightBlue1")
            #Manage_Frame.place(x=20,y=100,width=450,height=580)
            Manage_Frame.pack(side=TOP,fill=X)
            reg_btn=Button(Manage_Frame,text="Register",width=0,font=("times new roman",20,"bold")).grid(row=0,column=0,padx=1,pady=0)
            #Button(Manage_Frame,text="Login",width=10).grid(row=0,column=1,padx=10,pady=10)
            log_btn=Button(Manage_Frame,text="Login",width=0,font=("times new roman",20,"bold")).grid(row=0,column=1,padx=1,pady=0)

            #=========Manage1 Frame===========================

            Manage1_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="lightgreen")
            Manage1_Frame.place(x=20,y=160,width=450,height=520)

            m_title=Label(Manage1_Frame,text="Registration",bg="lightgreen",fg="black",font=("times new roman",30,"bold"))
            m_title.grid(row=0,columnspan=2,padx=110,pady=15)

            lbl_email=Label(Manage1_Frame,text="Email Availability",bg="lightgreen",fg="black",font=("times new roman",18,"bold"))
            lbl_email.grid(row=1,column=0,pady=10,padx=20,sticky="w")

            txt_email=Entry(Manage1_Frame,textvariable=self.Roll_No_var,width=30,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
            txt_email.grid(row=2,column=0,pady=0,padx=20,sticky="w")

            ver_btn=Button(Manage1_Frame,text="Verify",font=("times new roman",15,"bold")).grid(row=3,column=0,padx=80,pady=10,sticky="w")

            pro_btn=Button(Manage1_Frame,text="Proceed",font=("times new roman",15,"bold")).grid(row=3,column=0,padx=190,pady=10)

            lbl_image=Label(Manage1_Frame,text="Upload Picture",bg="lightgreen",fg="black",font=("times new roman",18,"bold"))
            lbl_image.grid(row=4,column=0,pady=10,padx=20,sticky="w")

            load_btn=Button(Manage1_Frame,text="Load Picture",command=self.fileDialog,font=("times new roman",15,"bold")).grid(row=4,column=0,padx=190,pady=10)

            #=========Detail Frame===========================

            Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="lightgreen")
            Detail_Frame.place(x=500,y=160,width=830,height=520)

            m_title1=Label(Detail_Frame,text="",bg="lightgreen")
            m_title1.grid(row=0,column=0,padx=110,pady=15)

            m_title=Label(Detail_Frame,text="Image",bg="lightgreen",fg="black",font=("times new roman",30,"bold"))
            m_title.grid(row=0,column=1,padx=110,pady=15)

            #=========Detail1 Frame===========================

            self.Detail1_Frame=Frame(Detail_Frame,bd=0,relief=RIDGE,bg="crimson")
            self.Detail1_Frame.place(x=80,y=80,width=665,height=410)
            #print("hi")
            #self.img.bind("<Button-1>",self.printcoords)
        except Exception as e:
            print(e)
    #=========Detail1 Frame image function===========================
    
    def fileDialog(self): 
        self.filename = filedialog.askopenfilename(initialdir =  "S:/", title = "Select A File", filetype =
        (("jpeg files","*.jpg"),("all files","*.*")) )
        if(self.filename!=""):
            load = Image.open(self.filename)
            render = ImageTk.PhotoImage(load)
            self.img = Label(self.Detail1_Frame, image=render)
            self.img.image = render
            self.img.place(x=3, y=3 ,width=658, height=404)
            self.img.bind("<Button-1>",self.printcoords)
            #self.Detail1_Frame.config(scrollregion=self.Detail1_Frame.bbox(ALL))
        #function to be called when mouse is clicked
    def printcoords(self,event):
        #outputting x and y coords to console
        #print (event.x,event.y)
        g=str(event.x)
        f=str(event.y)
        g=g+" "+f
        messagebox.showerror("Error",g)
        #mouseclick event
           

root=Tk()
obj =Student(root)
root.mainloop()


             #=========Register Frame===========================

            self.canRegister=Canvas(self.root,bd=0,relief=RIDGE,bg="lightgreen")
            self.canRegister.place(x=20,y=540,width=300,height=80)

            lbl_exit=Label(self.canRegister,text ="REGISTER\nTO DB",bg="LightBlue1",fg="black",font=("times new roman",12,"bold"))
            lbl_exit.place(x=0,y=0,width=104,height=44)
            reg_btn=Button(self.canRegister,text="REGISTER",font=("times new roman",15,"bold")).place(x=178,y=0)
            
             #=========Save Frame===========================

            self.canSave=Canvas(self.root,bd=0,relief=RIDGE,bg="lightgreen")
            self.canSave.place(x=420,y=532,width=200,height=70)

            lbl_exit=Label(self.canSave,text ="SAVE",bg="LightBlue1",fg="black",font=("times new roman",15,"bold"))
            lbl_exit.place(x=0,y=20,width=60)
            save_btn=Button(self.canSave,text="SAVE",font=("times new roman",15,"bold")).place(x=125,y=10)
            self.canSave.create_line(3,30,200,30)