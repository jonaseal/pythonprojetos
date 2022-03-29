from email.mime import audio
from linecache import getline
from multiprocessing.connection import wait
from selenium import webdriver
import pyautogui
import time
import pyttsx3 as pt
import speech_recognition as sr
import win32com.client as win32
import youtube_dl

texto1 = 'Olá Júnior, bem vindo. Qual música deseja baixar?'

textofalado = pt.init()
textofalado.say(texto1)
textofalado.runAndWait()

musica = input("Música: ")


navegador = webdriver.Chrome()
navegador.get('https://www.youtube.com/results?search_query={}'.format(musica))


link_webelement = navegador.find_element_by_css_selector('div#contents ytd-item-section-renderer>div#contents a#thumbnail')
link = link_webelement.get_attribute('href')
navegador.get(link)

video_url = navegador.current_url
video_info = youtube_dl.YoutubeDL().extract_info(url = video_url,download=False)
filename = f"{video_info['title']}.mp3"
options={
    'format':'bestaudio/best',
    'keepvideo':False,
    'outtmpl':filename,
    }

with youtube_dl.YoutubeDL(options) as ydl:
    ydl.download([video_info['webpage_url']])
    print("Download complete... {}".format(filename))

