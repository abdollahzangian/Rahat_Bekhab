from pyautogui import click, press, typewrite




def type_message(message):
    click(1094,685)
    typewrite(message)
    press("enter")

type_message("khaste nabashid")
    

