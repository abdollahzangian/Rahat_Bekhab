import os 
import tkinter as tk
import tkinter.font as tkFont
import datetime
import webbrowser



# the functions to kill procces of "adobe conncet" program 
def close_program(): 
         os.system("taskkill /f /im connect.exe")
         

# main functions to check the entry time and close "adobe conncet" program
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

def open_link(url):
        webbrowser.open_new(url)   

# design GUI 
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


        #setting "ساعت " label
        lbl_hour=tk.Label(root)
        ft = tkFont.Font(family='TAHOMA',size=13)
        lbl_hour["font"] = ft
        lbl_hour["fg"] = "#333333"
        lbl_hour["justify"] = "center"
        lbl_hour["text"] = "ساعت"
        lbl_hour.place(x=90,y=60,width=89,height=45)

        #setting "ساعت " entry
        self.saat=tk.StringVar()
        entry_hour= tk.Entry(root,textvariable=self.saat)
        entry_hour["borderwidth"] = "1px"
        ft = tkFont.Font(family='TAHOMA',size=10)
        entry_hour["font"] = ft
        entry_hour["fg"] = "#333333"
        entry_hour["justify"] = "center"
        entry_hour.place(x=160,y=70,width=50,height= 20)
        
        #setting "دقیقه " label
        lbl_minute=tk.Label(root)
        ft = tkFont.Font(family='TAHOMA',size=13)
        lbl_minute["font"] = ft
        lbl_minute["fg"] = "#333333"
        lbl_minute["justify"] = "center"
        lbl_minute["text"] = "دقیقه"
        lbl_minute.place(x=220,y=70,width=50,height=25)

        #setting "دقیقه " entry
        self.daghigh=tk.StringVar()
        entry_minute=tk.Entry(root,textvariable=self.daghigh)
        entry_minute["borderwidth"] = "1px"
        ft = tkFont.Font(family='TAHOMA',size=10)
        entry_minute["font"] = ft
        entry_minute["fg"] = "#333333"
        entry_minute["justify"] = "center"
        entry_minute.place(x=270,y=70,width=50,height=20)
        
        #setting "فعال کردن " button
        btn_active=tk.Button(root)
        btn_active["activebackground"] = "#126e9c"
        btn_active["bg"] = "#1e90ff"
        ft = tkFont.Font(family='TAHOMA',size=8)
        btn_active["font"] = ft
        btn_active["fg"] = "#000000"
        btn_active["justify"] = "center"
        btn_active["text"] = "فعال کردن"
        btn_active.place(x=170,y=120,width=60,height=20)
        btn_active["command"] = self.btn_active_command
       
        #setting "خروج " button
        btn_exit=tk.Button(root)
        btn_exit["activebackground"] = "#ea2617"
        btn_exit["bg"] = "#e62a2a"
        ft = tkFont.Font(family='TAHOMA',size=10)
        btn_exit["font"] = ft
        btn_exit["fg"] = "#000000"
        btn_exit["justify"] = "center"
        btn_exit["text"] = "خروج"
        btn_exit.place(x=240,y=120,width=40,height=20)
        btn_exit["command"] = self.btn_exit_command

        #setting "راحت برو بخواب " label
        lbl_header=tk.Label(root)
        ft = tkFont.Font(family='TAHOMA',size=15)
        lbl_header["font"] = ft
        lbl_header["fg"] = "#333333"
        lbl_header["justify"] = "center"
        lbl_header["text"] = " (: راحت برو بخواب "
        lbl_header.place(x=70,y=10,width=240,height=42)

        #setting " A.zangian طراحی شده توسط " label
        lbl_made_by=tk.Label(root)
        ft = tkFont.Font(family='TAHOMA',size=10)
        lbl_made_by["font"] = ft
        lbl_made_by.bind("<Button-1>", lambda e: open_link("https://github.com/abdollahzangian/Rahat_Bekhab"))
        lbl_made_by["fg"] = "blue"
        lbl_made_by["justify"] = "center"
        lbl_made_by["text"] = " A.zangian طراحی شده توسط"
        lbl_made_by.place(x=20,y=140,width=190,height=30)
        lbl_made_by.config(cursor="heart")
        # chenge style when hover on lable " A.zangian طراحی شده توسط"
        def Enter_style(e):
            lbl_made_by["fg"]="red"
        def Leave_style(e):
            lbl_made_by["fg"]="blue"


        lbl_made_by.bind("<Enter>", Enter_style)
        lbl_made_by.bind("<Leave>", Leave_style)

        
        


    def btn_active_command(self):
        check(self.saat.get(),self.daghigh.get())
        

    def btn_exit_command(self):
        root.destroy()

    


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()











