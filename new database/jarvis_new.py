import pyttsx3  
import speech_recognition as sr      
import datetime
import wikipedia 
import webbrowser
import random
import sys
import time
import os
import os.path
import requests  
import pywikihow   
from requests import get    
import smtplib 
from time import sleep
import pyjokes         
import pyautogui   
from time import sleep    
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import instaloader 
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from bs4 import BeautifulSoup
import pywhatkit as kit
import wolframalpha
from supergui8 import Ui_Widget

"""
IN PLACEOF PYTTSX3 WE CAN ALSO USE WIN32COM.CLIENT

# Python program to convert 
# text to speech 
  
# import the required module from text to speech conversion 
import win32com.client 
  
# Calling the Disptach method of the module which  
# interact with Microsoft Speech SDK to speak 
# the given input from the keyboard 
  
speaker = win32com.client.Dispatch("SAPI.SpVoice") 
  
while 1: 
    print("Enter the word you want to speak it out by computer") 
    s = input() 
    speaker.Speak(s) 
  
# To stop the program press 
# CTRL + Z 
"""


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices');
# print(voices[0].id)
engine.setProperty('voices', voices[0].id)
state = None
#text to speech
def speak(audio):
    jarvis.updateMovieDynamically('speaking')
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# def speak(audio):
#     speaker = Dispatch("SAPI.SpVoice")
#     print(audio)
#     speaker.Speak(audio)



#to wish
def wish():
    jarvis.updateMovieDynamically('speaking')
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if hour >= 0 and hour <= 12:
        speak(f"good morning, its {tt}")
        jarvis.terminalPrint(f"good morning, its {tt}")
        
    elif hour >= 12 and hour <= 18:
        speak(f"good afternoon, its {tt}")
        jarvis.terminalPrint(f"good afternoon, its {tt}")
    else:
        speak(f"good evening, its {tt}")
        jarvis.terminalPrint(f"good evening, its {tt}")
    speak("i am online sir. please tell me how may i help you")
    jarvis.terminalPrint("i am online sir. please tell me how may i help you")


    
#to send email
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('lohitlohit84@gmail.com', 'lohit12345*')
    server.sendmail('lohit2067@gmail.com', to, content)
    server.close()
import fitz  # PyMuPDF

def read_pdf(file_path):
    """
    Reads the text content of a PDF file and prints it.
    
    :param file_path: The path to the PDF file.
    """
    try:
        # Open the PDF file
        pdf_document = fitz.open(file_path)

        # Iterate through each page
        for page_num in range(pdf_document.page_count):
            # Get the page
            page = pdf_document[page_num]

            # Extract text from the page
            text = page.get_text()

            # Print or use the text as needed
            print(f"Page {page_num + 1}:\n{text}\n")

        # Close the PDF file
        pdf_document.close()

    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage
pdf_file_path = "path/to/your/file.pdf"
read_pdf(pdf_file_path)

#for news updates
def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=83263a48521a48a797182dbc3926e513'

    main_page = requests.get(main_url).json()
    # print(main_page)
    articles = main_page["articles"]
    # print(articles)
    head = []
    day=["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        # print(f"today's {day[i]} news is: ", head[i])
        speak(f"today's {day[i]} news is: {head[i]}")
  # def Sweather():
#     ipAdd = requests.get('https://api.ipify.org').text
#     print(ipAdd)
#     url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
#     geo_requests = requests.get(url)
#     geo_data = geo_requests.json()
#     # print(geo_data)
#     city = geo_data['city']
#     api_key = "30b2e680ad9c7790ec02fdb4f97f4573" #generate your own api key from open weather
#     base_url = "http://api.openweathermap.org/data/2.5/weather?"
#     city_name = (f'{city}')
#     complete_url = base_url + "appid=" + api_key + "&q=" + city_name
#     response = requests.get(complete_url)
#     x = response.json()
#     if x["cod"] != "404":
#         y = x["main"]
#         current_temperature = y["temp"]
#         # current_pressure = y["pressure"]
#         # current_humidiy = y["humidity"]
#         z = x["weather"]
#         weather_description = z[0]["description"]
#         r = ("outside " + " the Temperature is " +
#              str(int(current_temperature - 273.15)) + " degree celsius " +
#              ", atmospheric pressure " + str(current_pressure) + " hpa unit" +
#              ", humidity is " + str(current_humidiy) + " percent"
#              " and " + str(weather_description))
#         speak(r)
#     else:
#         speak(" City Not Found ")


class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def takecommand(self):
        jarvis.updateMovieDynamically('listening')
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("listening...")
            jarvis.terminalPrint("listening...")
            r.pause_threshold = 1
            r.energy_threshold = 300
            audio = r.listen(source,0,4)
            r.adjust_for_ambient_noise(source)
            # audio = r.listen(source)
            # audio = r.listen(source,timeout=4,phrase_time_limit=7)

        try:
            jarvis.updateMovieDynamically('loading')
            print("Recognizing...")
            jarvis.terminalPrint("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"user said: {query}")
            jarvis.terminalPrint(f"user said: {query}")

        except Exception as e:
            speak("Say that again please...")
            jarvis.terminalPrint("Say that again please...")
            return "none"
        query = query.lower()
        return query
    def run(self):
        self.TaskExecution()
        #speak(say wakeup to continue)
        # while True:
        #     self.query = self.takecommand()
        #     if "wake up" in self.query or "are you there" in self.query or "hello" in self.query:
        #         self.TaskExecution()

                        

    def TaskExecution(self):
        wish()
        while True:
            self.query = self.takecommand()

            #logic building for tasks

            if "open notepad" in self.query:
                npath = "C:\\Windows\\system32\\notepad.exe"
                os.startfile(npath)

            elif "open adobe reader" in self.query:
                apath = "C:\\Program Files (x86)\\Adobe\\Reader 11.0\\Reader\\AcroRd32.exe"
                os.startfile(apath)

            elif "open command prompt" in self.query:
                os.system("start cmd")
                pyautogui.write('curl parrot.live')
                pyautogui.press('enter')

            elif "take a photo" in self.query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("SMILE")
                    speak('your sooo cute ')
                    pyautogui.press("enter")
                    pyautogui.press('enter')
            elif 'pdf' in self.query:
                speak('ok sir reading your favorite comic book sir')
                
            elif "play music" in self.query:
                music_dir = "C:\\Users\\lohit\\Music"
                songs = os.listdir(music_dir)
                # rd = random.choice(songs)
                for song in songs:
                    if song.endswith('.mp3'):
                        os.startfile(os.path.join(music_dir, song))

            elif 'how to' in self.query:
             from pywikihow import search_wikihow
             speak('getting datta from internet')
             jarvis.terminalPrint('getting data from internet')
             op = self.query.replace('jarvis','')
             max_result = 1
             how_to_func = search_wikihow(op,max_result)
             assert len(how_to_func) ==1
             how_to_func[0].print()
             speak(how_to_func[0].summary)
            

            elif "ip address" in self.query:
                ip = '117.196.148.15'
                speak(f"your IP address is {ip}")

            elif "wikipedia" in self.query:
                speak("searching wikipedia....")
                jarvis.terminalPrint("searching wikipedia....")
                self.query = self.query.replace("wikipedia","")
                results = wikipedia.summary(self.query, sentences=2)
                speak("according to wikipedia")
                speak(results)
                jarvis.terminalPrint(results)
                #print(results)                                                                                  
            elif 'open youtube' in self.query:
                speak('what will you like to watch')
                jarvis.terminalPrint('what will you like to watch')
                self.query = self.takecommand().lower()
                kit.playonyt(f'{self.query}')
            elif 'youtube search' in self.query:
               from SearchNow import searchYoutube
               searchYoutube(self.query)
            
            elif "open facebook" in self.query:
             webbrowser.open("www.facebook.com")

            elif "open stackoverflow" in self.query:
                webbrowser.open("www.stackoverflow.com")

            elif "open google" in self.query:
                speak("sir, what should i search on google")
                jarvis.terminalPrint("sir, what should i search on google")
                cm = self.takecommand()
                webbrowser.open(f"{cm}")
            elif 'google search' in self.query:
                 from SearchNow import searchGoogle
                 searchGoogle(self.query)

            
            elif "play a game" in self.query:
                    from game import game_play
                    game_play()
            # elif "song on youtube" in self.query:
            #     kit.playonyt("see you again")
            
            elif '' in self.query:
                ('sir due to many noises its hard to detect ur voice sir')
            elif "email" in self.query:
                 try:
                    speak("what should i say?")
                    content = self.takecommand()
                    to = "lohit2067@gmail.com"
                    sendEmail(to,content)
                    speak("Email has been sent to avinash")

                 except Exception as e:
                     print(e)
                     speak("sorry sir, i am not able to sent this mail to avi")

            elif "you can sleep" in self.query or "sleep now" in self.query:
                speak("okay sir, i am going to sleep you can call me anytime.")
                jarvis.terminalPrint("okay sir, i am going to sleep you can call me anytime.")
                # sys.exit()
                # gifThread.exit()
                break
                
            elif 'tell about friend' in self.query:
                speak('he is gaaju boy name jeeva')

            #to close any application
            elif "close notepad" in self.query:
                speak("okay sir, closing notepad")
                jarvis.terminalPrint("okay sir, closing notepad")
                os.system("taskkill /f /im notepad.exe")

            #to set an alarm
            elif "set alarm" in self.query:
                nn = int(datetime.datetime.now().hour)
                if nn==22: 
                    music_dir = 'E:\\music'
                    songs = os.listdir(music_dir)
                    os.startfile(os.path.join(music_dir, songs[0]))
            #to find a joke
            elif "joke" in self.query:
                joke = pyjokes.get_joke()
                speak(joke)
                jarvis.terminalPrint(joke)
            elif "play video" in self.query:
                pyautogui.press("k")
                speak("video played")
                jarvis.terminalPrint("video played")
            elif "mute video" in self.query:
                pyautogui.press("m")
                speak("video muted")
                jarvis.terminalPrint("video muted")
            elif "mute" in self.query:
                pyautogui.press("volumemute")

                


            elif "volume up" in self.query:
                speak("Turning volume up,sir")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                
            elif "volume down" in self.query:
                speak("Turning volume down, sir")
                pyautogui.press('volumedown')
                pyautogui.press('volumedown')
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                
            elif "shutdown" in self.query:
                 speak('access granted activating shutdown ,system ,protocol,5,4,3,2,1,0')
                 os.system("shutdown /s /t 5")

            elif "restart the system" in self.query:
                speak('activating restart system protocol sir')
                os.system("shutdown /r /t 5")

            elif "sleep the system" in self.query:
             speak('going to sleep sir')
             os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

            elif "hello" in self.query or "hey" in self.query:
                speak("hello sir, may i help you with something.")
                jarvis.terminalPrint("hello sir, may i help you with something.")
            
            elif "how are you" in self.query:
                speak("i am fine sir, what about you.")
                jarvis.terminalPrint("i am fine sir, what about you.")

            elif "thank you" in self.query or "thanks" in self.query:
                speak("it's my pleasure sir.")
                jarvis.terminalPrint("it's my pleasure sir.")
            
            elif 'open' in self.query:
                self.query = self.query. replace("open","")
                self.query = self.query.replace("jarvis","")
                pyautogui.press ("super")
                pyautogui.typewrite(self.query)
                pyautogui.sleep (2)
                pyautogui.press("enter")


            ###################################################################################################################################
            ###########################################################################################################################################



            elif 'switch the window' in self.query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")
                    

            elif "news" in self.query:
                speak("please wait sir, feteching the latest news")
                jarvis.terminalPrint("please wait sir, feteching the latest news")
                news()
                 

            elif "email to friend" in self.query:
                
                speak("sir what should i say")
                self.query = self.takecommand()
                if "send a file" in self.query:
                    email = 'lohitlohit84@gmail.com' # Your email
                    password = 'lohit12345*' # Your email account password
                    send_to_email = 'lohit2067@gmail.com' # Whom you are sending the message to
                    speak("okay sir, what is the subject for this email")
                    self.query = self.takecommand()
                    subject = self.query   # The Subject in the email
                    speak("and sir, what is the message for this email")
                    self.query2 = self.takecommand()
                    message = self.query2  # The message in the email
                    speak("sir please enter the correct path of the file into the shell")
                    file_location = input("please enter the path here")    # The File attachment in the email

                    speak("please wait,i am sending email now")

                    msg = MIMEMultipart()
                    msg['From'] = email
                    msg['To'] = send_to_email
                    msg['Subject'] = subject

                    msg.attach(MIMEText(message, 'plain'))

                    # Setup the attachment
                    filename = os.path.basename(file_location)
                    attachment = open(file_location, "rb")
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(attachment.read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

                    # Attach the attachment to the MIMEMultipart object
                    msg.attach(part)

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login(email, password)
                    text = msg.as_string()
                    server.sendmail(email, send_to_email, text)
                    server.quit()
                    speak("email has been sent to avinash")

                else:                
                    email = 'lohitlohit84@gmail.com' # Your email
                    password = 'lohit12345*' # Your email account password
                    send_to_email = 'ramamseeta01@gmail.com' # Whom you are sending the message to
                    message = self.query # The message in the email

                    server = smtplib.SMTP('smtp.gmail.com', 587) # Connect to the server
                    server.starttls() # Use TLS
                    server.login(email, password) # Login to the email server
                    server.sendmail(email, send_to_email , message) # Send the email
                    server.quit() # Logout of the email server
                    speak("email has been sent to avinash")


            ##########################################################################################################################################
            ###########################################################################################################################################

            elif "calculate" in self.query:
                    from Calculatenumbers import WolfRamAlpha
                    from Calculatenumbers import Calc
                    self.query = self.query.replace("calculate","")
                    self.query = self.query.replace("jarvis","")
                    Calc(self.query)
                    jarvis.terminalPrint(Calc(self.query))
            
            elif "scroll" in self.query:
                pyautogui.scroll(1000)
            elif "open notepad" in self.query:
                pyautogui.hotkey('win')
                time.sleep(1)
                pyautogui.write('notepad')
                time.sleep(1)
                pyautogui.press('enter')
                time.sleep(1)
                pyautogui.write(self.query, interval = 0.1)
            elif 'minimise' in self.query:
                pyautogui.hotkey('win'+'d')
                time.sleep(1)
                pyautogui.press('')
            elif 'close tab' in self.query:
                pyautogui.hotkey('ctrl', 'w')
                                
            elif 'previous tab' in self.query:
                pyautogui.hotkey('ctrl', 'shift', 'tab')
            #-----------------To find my location using IP Address

            elif "where I am" in self.query or "where we are" in self.query:
                speak("wait sir, let me check")
                try:
                    ipAdd = "117.196.148.15"
                    url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                    geo_requests = requests.get(url)
                    geo_data = geo_requests.json()
                    # print(geo_data)
                    city = geo_data['city']
                    # state = geo_data['state']
                    country = geo_data['country']
                    speak(f"sir i am not sure, but i think we are in {city} city of {country} country")
                except Exception as e:
                    speak("sorry sir, Due to network issue i am not able to find where we are.")
                    pass


            

            #-------------------To check a instagram profile----
            elif "Instagram profile" in  self.query or "profile on instagram" in self.query:
                speak("sir please enter the user name correctly.")
                name = input("Enter username here:")
                webbrowser.open(f"www.instagram.com/{name}")
                speak(f"Sir here is the profile of the user {name}")
                time.sleep(5) 
                speak("sir would you like to download profile picture of this account.")
                jarvis.terminalPrint("sir would you like to download profile picture of this account.")
                condition = self.takecommand()
                if "yes" in condition:
                    mod = instaloader.Instaloader() #pip install instadownloader
                    mod.download_profile(name, profile_pic_only=True)
                    speak("i am done sir, profile picture is saved in our main folder. now i am ready for next command")
                else:
                    pass
            elif 'movie' in self.query:
                speak('playing recently released movie from tamilyogi.com')
                jarvis.terminalPrint('playing recently released movie from tamilyogi.com')
                npath = "C:/Users/lohit/Downloads/Video/leo movie.ts" 
                os.startfile(npath)
            #-------------------  To take screenshot -------------
            elif "take screenshot" or "take a screenshot" in self.query:
                speak("sir, please tell me the name for this screenshot file")
                jarvis.terminalPrint("sir, please tell me the name for this screenshot file")
                name = self.takecommand()
                speak("please sir hold the screen for few seconds, i am taking sreenshot")
                jarvis.terminalPrint("please sir hold the screen for few seconds, i am taking sreenshot")
                time.sleep(3)
                img = pyautogui.screenshot()
                img.save(f"{name}.png")
                speak("i am done sir, the screenshot is saved in our main folder. now i am ready for next command")
                jarvis.terminalPrint("i am done sir, the screenshot is saved in our main folder. now i am ready for next command")
                speak("sir, do you have any other work")
                jarvis.terminalPrint("sir, do you have any other work")
           

            #--------------------- To Hide files and folder ---------------
            elif "hide all files" in self.query or "hide this folder" in self.query or "visible for everyone" in self.query:
                speak("sir please tell me you want to hide this folder or make it visible for everyone")
                condition = self.takecommand()
                if "hide" in condition:
                    os.system("attrib +h /s /d") #os module
                    speak("sir, all the files in this folder are now hidden.")                

                elif "visible" in condition:
                    os.system("attrib -h /s /d")
                    speak("sir, all the files in this folder are now visible to everyone. i wish you are taking this decision in your own peace.")
                    
                elif "leave it" in condition or "leave for now" in condition:
                    speak("Ok sir")

            elif "temperature" in self.query:
                search = "weather in delhi"
                url = f"https://www.google.com/search?q={search}"
                req = requests.get(url)
                save = BeautifulSoup(req.text,"html.parser")
                tempp = save.find("div",class_= "BNeawe").text
                speak(f"current {search} is {tempp}")


startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.pushButton_3.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)
        self.setWindowTitle("Friday - Lohit")
        self.setWindowIcon(QIcon("jarvis.png"))
        import ctypes
        myappid = 'lohit.app.friday.1.0'
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    def terminalPrint(self,text):
        self.ui.TERMINALOUTPUT.appendPlainText(text)








    def updateMovieDynamically(self,state):
        if state == 'speaking':
            self.ui.voice.raise_()
            self.ui.voice.show()
            self.ui.listen.hide()
            self.ui.loading.hide()
        elif state == 'listening':
            self.ui.listen.raise_()
            self.ui.listen.show()
            self.ui.voice.hide()
            self.ui.loading.hide()
        elif state == 'loading':
            self.ui.loading.raise_()
            self.ui.loading.show()
            self.ui.voice.hide()
            self.ui.loading.hide()

    def startTask(self):
        self.ui.movie = QtGui.QMovie("C:/Users/lohit/OneDrive/Documents/science_project/B.G/coding.gif")
        self.ui.coding.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("C:/Users/lohit/OneDrive/Documents/science_project/B.G/arc.gif")
        self.ui.arc.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("C:/Users/lohit/OneDrive/Documents/science_project/B.G/Ntuks.gif")
        self.ui.voice.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("C:/Users/lohit/OneDrive/Documents/science_project/B.G/listening.gif")
        self.ui.listen.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("C:/Users/lohit/OneDrive/Documents/science_project/B.G/loading.gif")
        self.ui.loading.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("C:/Users/lohit/OneDrive/Documents/science_project/B.G/blue energy.gif")
        self.ui.blue.setMovie(self.ui.movie)
        self.ui.movie.start()

        startExecution.start()

   

#self.textBrowser.setText("Hello world")
 #       self.textBrowser.setAlignment(QtCore.Qt.AlignCenter)

app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
sys.exit(app.exec_())
