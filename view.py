from tkinter import Tk, Button, Label, Entry, Frame, Toplevel, Text, Menu, StringVar
import tkinter.font as tkFont

class App(Tk):
    def __init__(self, callback1, callback2):
        super(App, self).__init__()
        self.callback1 = callback1
        self.callback2 = callback2
        self.title("صفحه اصلی")
        self.geometry("440x180")
        self.resizable(False,False)

        #setting "ساعت " label
        lbl_hour =Label(self)
        ft = tkFont.Font(family='TAHOMA', size=13)
        lbl_hour["font"] = ft
        lbl_hour["fg"] = "#333333"
        lbl_hour["justify"] = "center"
        lbl_hour["text"] = "ساعت"
        lbl_hour.place(x=90, y=60, width=89, height=45)

        #setting "ساعت " entry
        self.saat = StringVar() 
        entry_hour = Entry(self, textvariable = self.saat)
        entry_hour["borderwidth"] = "1px"
        ft = tkFont.Font(family ='TAHOMA', size=10)
        entry_hour["font"] = ft
        entry_hour["fg"] = "#333333"
        entry_hour["justify"] = "center"
        entry_hour.place(x = 160, y = 70, width = 50, height = 20)
        
        #setting "دقیقه " label
        lbl_minute = Label(self)
        ft = tkFont.Font(family = 'TAHOMA', size = 13)
        lbl_minute["font"] = ft
        lbl_minute["fg"] = "#333333"
        lbl_minute["justify"] = "center"
        lbl_minute["text"] = "دقیقه"
        lbl_minute.place(x = 220, y = 70, width = 50, height = 25)

        #setting "دقیقه " entry
        self.daghigh = StringVar()
        entry_minute = Entry(self, textvariable = self.daghigh)
        entry_minute["borderwidth"] = "1px"
        ft = tkFont.Font(family = 'TAHOMA', size = 10)
        entry_minute["font"] = ft
        entry_minute["fg"] = "#333333"
        entry_minute["justify"] = "center"
        entry_minute.place(x = 270, y = 70, width = 50, height = 20)
        
        #setting "فعال کردن " button
        btn_active = Button(self)
        btn_active["activebackground"] = "#126e9c"
        btn_active["bg"] = "#1e90ff"
        ft = tkFont.Font(family='TAHOMA', size = 8)
        btn_active["font"] = ft
        btn_active["fg"] = "#000000"
        btn_active["justify"] = "center"
        btn_active["text"] = "فعال کردن"
        btn_active.place(x = 170, y = 120, width = 60, height = 20)
        btn_active["command"] = self.btn_active_command
       
        #setting "خروج " button
        btn_exit=Button(self)
        btn_exit["activebackground"] = "#ea2617"
        btn_exit["bg"] = "#e62a2a"
        ft = tkFont.Font(family = 'TAHOMA', size = 10)
        btn_exit["font"] = ft
        btn_exit["fg"] = "#000000"
        btn_exit["justify"] = "center"
        btn_exit["text"] = "خروج"
        btn_exit.place(x = 240, y = 120, width = 40, height = 20)
        btn_exit["command"] = self.btn_exit_command

        #setting "راحت برو بخواب " label
        lbl_header = Label(self)
        ft = tkFont.Font(family = 'TAHOMA', size = 15)
        lbl_header["font"] = ft
        lbl_header["fg"] = "#333333"
        lbl_header["justify"] = "center"
        lbl_header["text"] = " (: راحت برو بخواب "
        lbl_header.place(x=70, y=10, width=240, height=42)

        #setting " A.Zangian طراحی شده توسط " label
        lbl_made_by=Label(self)
        ft = tkFont.Font(family='TAHOMA', size=10)
        lbl_made_by["font"] = ft
        lbl_made_by.bind("<Button-1>", lambda e: callback1("https://github.com/abdollahzangian/Rahat_Bekhab"))
        lbl_made_by["fg"] = "blue"
        lbl_made_by["justify"] = "center"
        lbl_made_by["text"] = " A.Zangian طراحی شده توسط"
        lbl_made_by.place(x=20, y=140, width=190, height=30)
        lbl_made_by.config(cursor="heart")
        # chenge style when hover on lable " A.zangian طراحی شده توسط"
        def Enter_style(e):
            lbl_made_by["fg"]="red"
        def Leave_style(e):
            lbl_made_by["fg"]="blue"

        lbl_made_by.bind("<Enter>", Enter_style)
        lbl_made_by.bind("<Leave>", Leave_style)

    def btn_active_command(self):
        self.callback2(self.saat.get(),self.daghigh.get())

    def btn_exit_command(self):
        self.destroy()
