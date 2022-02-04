import model
import view 
from tkinter import mainloop


menu = model.Core()

root = view.App(
    callback1=menu.open_link,
    callback2=menu.check
)
root = mainloop()
