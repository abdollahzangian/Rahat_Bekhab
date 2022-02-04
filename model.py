import datetime
from main import close_program
import webbrowser
import os

class Core:
        def __init__(self) -> None:
                self.hour = None
                self.minute = None
                self.command = None
                

        def close_program(self, command):
                program_name = "connect.exe"
                command = "taskkill /f /im "
                os.system(command + program_name)
                        
        def check(self, hour, minute):
                
                time=f"{hour}:{minute}:00"
                
                while True:
                        current_time=datetime.datetime.now()
                        now = current_time.strftime("%H:%M:%S")
                        print(now)
                        
                        if now == time:
                                close_program()
                                break


        def open_link(self, url):
                webbrowser.open_new(url)  

        