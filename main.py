import os 
import tkinter as tk
import tkinter.font as tkFont
import datetime




def close_program(): 
         os.system("taskkill /f /im connect.exe")
         


def check(saat,daghighe):
        print(saat)
        print(daghighe)
        time=f"{saat}:{daghighe}:00"
        print(time)
        while True:
             current_time=datetime.datetime.now()
             now = current_time.strftime("%H:%M:%S")
             print(now)
            
             if now == time :
                 print("0")
                 close_program()
                 break

            







class App:
    def __init__(self, root):
        #setting title
        root.title("صفحه اصلی")
        #setting window size
        width=443
        height=181
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_2=tk.Label(root)
        ft = tkFont.Font(family='TAHOMA',size=13)
        GLabel_2["font"] = ft
        GLabel_2["fg"] = "#333333"
        GLabel_2["justify"] = "center"
        GLabel_2["text"] = "ساعت "
        GLabel_2.place(x=90,y=60,width=89,height=45)


        self.saat=tk.StringVar()
        GLineEdit_895= tk.Entry(root,textvariable=self.saat)
        GLineEdit_895["borderwidth"] = "1px"
        ft = tkFont.Font(family='TAHOMA',size=10)
        GLineEdit_895["font"] = ft
        GLineEdit_895["fg"] = "#333333"
        GLineEdit_895["justify"] = "center"
        GLineEdit_895.place(x=160,y=70,width=50,height= 20)
        

        lbl_minute=tk.Label(root)
        ft = tkFont.Font(family='TAHOMA',size=13)
        lbl_minute["font"] = ft
        lbl_minute["fg"] = "#333333"
        lbl_minute["justify"] = "center"
        lbl_minute["text"] = "دقیقه"
        lbl_minute.place(x=220,y=70,width=50,height=25)

        self.daghigh=tk.StringVar()
        GLineEdit_656=tk.Entry(root,textvariable=self.daghigh)
        GLineEdit_656["borderwidth"] = "1px"
        ft = tkFont.Font(family='TAHOMA',size=10)
        GLineEdit_656["font"] = ft
        GLineEdit_656["fg"] = "#333333"
        GLineEdit_656["justify"] = "center"
        GLineEdit_656.place(x=270,y=70,width=50,height=20)
        
        GButton_953=tk.Button(root)
        GButton_953["activebackground"] = "#126e9c"
        GButton_953["bg"] = "#1e90ff"
        ft = tkFont.Font(family='TAHOMA',size=8)
        GButton_953["font"] = ft
        GButton_953["fg"] = "#000000"
        GButton_953["justify"] = "center"
        GButton_953["text"] = "فعال کردن"
        GButton_953.place(x=170,y=120,width=60,height=20)
        GButton_953["command"] = self.GButton_953_command
       

        GButton_424=tk.Button(root)
        GButton_424["activebackground"] = "#ea2617"
        GButton_424["bg"] = "#e62a2a"
        ft = tkFont.Font(family='TAHOMA',size=10)
        GButton_424["font"] = ft
        GButton_424["fg"] = "#000000"
        GButton_424["justify"] = "center"
        GButton_424["text"] = "خروج"
        GButton_424.place(x=240,y=120,width=40,height=20)
        GButton_424["command"] = self.GButton_424_command

        GLabel_826=tk.Label(root)
        ft = tkFont.Font(family='TAHOMA',size=15)
        GLabel_826["font"] = ft
        GLabel_826["fg"] = "#333333"
        GLabel_826["justify"] = "center"
        GLabel_826["text"] = " (: راحت برو بخواب "
        GLabel_826.place(x=70,y=10,width=240,height=42)

        GLabel_425=tk.Label(root)
        ft = tkFont.Font(family='TAHOMA',size=10)
        GLabel_425["font"] = ft
        GLabel_425["fg"] = "#333333"
        GLabel_425["justify"] = "center"
        GLabel_425["text"] = " A.zangian طراحی شده توسط"
        GLabel_425.place(x=20,y=140,width=190,height=30)
        
    def chars(self):
        print("command")
    def number(self):
        print("command")


    def chars(self):
        print("command")
    def number(self):
        print("command")


    def GButton_953_command(self):
        check(self.saat.get(),self.daghigh.get())
        
        
       



    def GButton_424_command(self):
        root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()











