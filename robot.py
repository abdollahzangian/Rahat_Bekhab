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

        pytesseract.pytesseract.tesseract_cmd = r"C:\Python39\Lib\site-packages\pytesseract"
        while True:
        
            process_area = ImageGrab.grab(bbox=(993, 577, 1365, 730))
            text = pytesseract.image_to_string(
                    cv2.cvtColor(np.array(process_area), cv2.COLOR_BGR2GRAY),
                    lang = "eng"
                )
            print(text)
            








    


