import requests
import telebot
import colorama
from bs4 import *
from colorama import init
from colorama import Fore, Back, Style
from LxmlSoup import LxmlSoup
from settings import *

html = requests.get(RECOURCE_URL).text
soup = BeautifulSoup(html, 'lxml')

links_list = []


for link in soup.find_all('a', class_='news-listing__item-link'):
    links_list.append(link.get('href'))


for link in links_list:
    html = requests.get(link)
    soup = BeautifulSoup(html.text, 'lxml')
    print(soup.find('h1', class_='article__title').text)
    print(soup.find('div', class_='article__body').text)
    print(f'-------------------------------------------------------------------------------------------')
















# bot = telebot.TeleBot(TELEGRAMM_TOKEN)
# @bot.message_handler(commands=['start'])
# def echo(message):
#     bot.send_message(message.chat.id, text='привет')
# bot.polling(none_stop=True)
