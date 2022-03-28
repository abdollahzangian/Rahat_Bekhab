import model
from time import sleep
from pyautogui import click, press, typewrite
import pytesseract 
import cv2
import numpy as np  
from PIL import ImageGrab


def type_message(message):

     #(1097,698) ---> text box adobe
     #(1340,693) ---> send message botton 
     click(1097,693)
     typewrite(message)
     press("enter")


def extractText():
        # point : 993, 577, 1365, 730
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        while True:
            process_area = ImageGrab.grab(include_layered_windows=False,bbox=(725, 577, 1365, 730))
            text = pytesseract.image_to_string(
                    cv2.cvtColor(np.array(process_area), cv2.COLOR_BGR2GRAY),
                    lang = "eng"
                )

            
            if "khaste nabashid" in text:
                type_message()
                sleep(1)
                model.Core.close_program()
                break
extractText()
