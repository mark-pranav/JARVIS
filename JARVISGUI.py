from JARVISUI import Ui_MainWindow
from PyQt5 import QtCore,QtWidgets,QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import pyttsx3
import speech_recognition as sr
import webbrowser
import pywhatkit
import os
import datetime
from playsound import playsound
import wikipedia
import pyautogui
import pyjokes
from PyDictionary import PyDictionary as Diction
import sys

engine=pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voices',voices[0].id)
engine.setProperty('rate', 170)



def Speak(audio):
    print("   ")
    engine.say(audio)
    print(f": {audio}")
    print("   ")
    engine.runAndWait()

class MainThread (QThread):
    
    def __init__(self):
        super(MainThread,self).__init__()
        
    def run(self):
        self.taskExe()
        
    def takecommand (self):
        command = sr.Recognizer()
        with sr.Microphone() as source:
            print ("Listening.....")
            command.pause_threshold =1
            audio = command.listen(source)
            
            try:
                print ("Recognizing...")
                query = command.recognize_google(audio,language='en-in')
                print (f"You said : {query}")
                return query.lower()
                
            except Exception as Error :
                return "none"
            
            
    
    
    def taskExe(self):
        query=" "
    
        def Music():
            Speak("Tell  song ...!")
            musicName = self.takecommand(self)
            
            if'hum to deewane' in musicName :
                os.startfile('C:\\Users\\HP\Downloads\\Hum Toh Deewane Elvish Yadav Urvashi Rautela Yasser Desai Rajat Nagpal Rana Anshul Garg.mp3')
                
            else:
                pywhatkit.playonyt(musicName)
                
            Speak("Enjoy.......!")
        
        def OpenAPP():
            Speak(" OK Sir , Hold A minute")
            
            if 'Google classroom' in query:
                os.startfile('"C:\Program Files\BraveSoftware\Brave-Browser\Application\chrome_proxy.exe"  --profile-directory=Default --app-id=kjcjfjccmpngedeildfijeanhihmolck')
                
            elif 'Canva' in query :
                os.startfile('C:\\Users\\HP\\AppData\\Local\\Programs\\Canva\\Canva.exe')
                
            elif 'Brave' in query :
                os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs')
            
            Speak("Done Boss , What's next ?")       
            
    # def ytautomation():
        
    #     Speak ("What's your command ?")
    #     comm=takecommand()
        
    #     if 'pause' in query:
    #         keyboard.press('space bar')
            
    #     if 'restart' in query:
    #         keyboard.press('0')
        
        def dict ():
            Speak("Tell me the problem!")
            prob = self.takecommand()
            
            if 'meaning' in prob:
                probl = probl.replace ("What is the" ,"")
                probl = probl.replace ("Jarvis" ,"")
                probl = probl.replace ("of")
                probl = probl.replace ("meaning")
                result = Diction.meaning(probl)
                Speak (f"the meaning of {probl} is {result}")
                
            elif 'synonym' in probl:
                probl = probl.replace ("What is the" ,"")
                probl = probl.replace ("Jarvis" ,"")
                probl = probl.replace ("of")
                probl = probl.replace ("synonym")
                result = Diction.synonym(probl)
                Speak (f"the synonym of {probl} is {result}")
                
            elif 'antonym' in probl:
                probl = probl.replace ("What is the" ,"")
                probl = probl.replace ("Jarvis" ,"")
                probl = probl.replace ("of")
                probl = probl.replace ("antonym")
                result = Diction.antonym(probl)
                Speak (f"the antonym of {probl} is {result}")
                
            Speak("Exit Dictionary")
                
                
                
        while True:
            
            self.query = self.takecommand()
            
            if 'hello' in self.query :
                Speak("Hello sir , I am JARVIS .")
                Speak ("Your personal AI Assistant")
                Speak ("How May I Help you ?")
                
            elif 'how are you jarvis' in self.query :
                Speak ("I am Fine Sir !")
                Speak ("Whats aboiut you")
                
            elif 'you need break ' in self.query :
                Speak("Ok sir , You can call me anytime")
                break
                
            
            elif 'bye' in self.query :
                Speak ("OK Sir , Bye , See you soon ")
                break
                
            elif 'Who is your girlfriend ?'in self.query :
                Speak ("I will have arrange marriage") 
                
            elif 'Main achaa hoon na ?' in self.query :
                Speak ("bohot achhe ho sir lekin mere se nahi ")
                
            elif 'open youtube' in self.query :
                Speak ("OK Sir , this is what I found for your Search ....!")
                self.query = self.query.replace("JARVIS","")
                self.query = self.query.replace("Youtube Search","")
                web = ' https://www.youtube.com'
                webbrowser.open(web)
                Speak ("Done Sir !")
                
            elif 'Open Google ' in self.query:
                Speak("This is what I found for your search...!")
                self.query = self.query.replace("JARVIS","")
                self.query = self.query.replace("Google Search","")
                pywhatkit.search(query)
                Speak("Done sir !!!!!")
                
            # elif 'Open Wikipedia OR Search in Wikipedia' in query :
            #     Speak ("Ohk , lets wait for second.....!")
            #     query = query.replace("JARVIS","")
            #     query = query.replace("Google Search","")
            
            elif 'Website' in self.query :
                Speak("Ok Sir ,Launching....!")
                query = query.replace("Jarvis" ,"")
                query = query.replace("website" ,"")
                query = query.replace(" " ,"")
                web1 = query.replace("Open","")
                web2 = 'https://www.' + web1 +'.com'
                webbrowser.open(web2)
                Speak ("Launching....")
            
            elif 'launch' in self.query :
                Speak ("tell me the name of the website ?")
                name = self.takecommand()
                web = 'https://www.' + name + '.com'
                webbrowser.open(web)
                Speak ("Done Sir !!!")
                
            elif 'music' in self.query:
                Music()
                
            elif 'wikipeadia' in self.query :
                Speak("Searching Wikipedia.....!")
                query = query.replace("JARVIS","")
                query = query.replace ("Wikipedia","")
                wiki = wikipedia.summary(query,2)
                Speak(f"According to wikipedia : {wiki}")
                
            elif 'Screenshot' in self.query:
                kk=pyautogui.screenshot()
                kk.save('C:\\Users\\HP\\Pictures\\Screenshots')
                Speak(" Done .. Boss!")
                
            elif 'Open google classroom' in self.query:
                OpenAPP()  
                
            elif 'Open canva' in self.query:
                OpenAPP() 
            
            elif 'Open brave' in self.query:
                OpenAPP() 
                
            elif 'joke' in self.query:
                get = pyjokes.get_joke()
                Speak(get)
            
            elif 'dictionary' in query:
                dict()  
                
            elif 'alarm' in query:
                Speak("Enter the Time !")
                time= input ("Set Time:")
                
                while True:
                    Time_AC = datetime.datetime.now()
                    now = Time_AC.strftime("%H:%M:%S")
                    
                    if now == time:
                        Speak ("Time to Wake up Boss , Get Ready")
                        playsound('kesari.mp3')
                        Speak("Alarm closed")
                        
                    elif now>time:
                        break


startFunctions = MainThread()

class gui_strart (QMainWindow):
    
    def __init__(self):
        super ().__init__()
        self.jarvis_UI = Ui_MainWindow()
        self.jarvis_UI.setupUi(self)
        
        self.jarvis_UI.pushButton.clicked.connect(self.startFunc)
        self.jarvis_UI.pushButton_2.clicked.connect(self.close)
        
    def startFunc(self):
        self.jarvis_UI.movies_2 = QtGui.QMovie("D:\AIProject\GUI\GUI_FOLDER\Iron_Template_1.gif")
        self.jarvis_UI.label_2.setMovie(self.jarvis_UI.movies_2)
        self.jarvis_UI.movies_2.start()
        
        self.jarvis_UI.movies_3 = QtGui.QMovie("D:\AIProject\GUI\GUI_FOLDER\initial.gif")
        self.jarvis_UI.label_3.setMovie(self.jarvis_UI.movies_3)
        self.jarvis_UI.movies_3.start()
        
        self.jarvis_UI.movies_4 = QtGui.QMovie("D:\AIProject\GUI\GUI_FOLDER\loading_1.gif")
        self.jarvis_UI.label_4.setMovie(self.jarvis_UI.movies_4)
        self.jarvis_UI.movies_4.start()
        
        self.jarvis_UI.movies_6 = QtGui.QMovie("D:\AIProject\GUI\GUI_FOLDER\Code_Template.gif")
        self.jarvis_UI.label_6.setMovie(self.jarvis_UI.movies_6)
        self.jarvis_UI.movies_6.start()
        
        self.jarvis_UI.movies_7 = QtGui.QMovie("D:\AIProject\GUI\GUI_FOLDER\Earth.gif")
        self.jarvis_UI.label_7.setMovie(self.jarvis_UI.movies_7)
        self.jarvis_UI.movies_7.start()
        
        self.jarvis_UI.movies_8 = QtGui.QMovie("D:\AIProject\GUI\GUI_FOLDER\Hero_Template.gif")
        self.jarvis_UI.label_8.setMovie(self.jarvis_UI.movies_8)
        self.jarvis_UI.movies_8.start()
        
        self.jarvis_UI.movies_9= QtGui.QMovie("D:\AIProject\GUI\GUI_FOLDER\Health_Template.gif")
        self.jarvis_UI.label_9.setMovie(self.jarvis_UI.movies_9)
        self.jarvis_UI.movies_9.start()
        
        startFunctions.start()
    
    
Gui_app = QApplication(sys.argv)
Gui_Jarvis = gui_strart()
Gui_Jarvis.show()
exit(Gui_app.exec())
        
        
        
        
        
        
        
        
        

