from email.mime import audio
from linecache import getline
from multiprocessing.connection import wait
from selenium import webdriver
import pyautogui
import time
import pyttsx3 as pt
import speech_recognition as sr
import win32com.client as win32

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

navegador.get('https://x2download.com/pt5/download-youtube-to-mp3')

inputsite = navegador.find_element_by_xpath('//form/input')
inputsite.send_keys(link)

botaomp3 = navegador.find_element_by_xpath('//*[@id="search-form"]/button')
botaomp3.click()

time.sleep(3)
getlink= navegador.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div[2]/div/div/div/div/div/div[1]/button')
getlink.click()
time.sleep(5)
baixar = navegador.find_element_by_xpath('//*[@id="asuccess"]')
baixar.click()

aguardar = input("aguardando...")




