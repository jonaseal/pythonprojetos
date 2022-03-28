import requests
import selenium
from parsel import Selector
from bs4 import BeautifulSoup
from selenium import webdriver



navegador = webdriver.Chrome()
navegador.get('https://x2download.com/pt5/download-youtube-to-mp3')

elemento = navegador.find_element_by_xpath("//body").text

print(elemento)


