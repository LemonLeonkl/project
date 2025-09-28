from bs4 import BeautifulSoup
import requests
import pandas as pd

news_links = []

def get_news():
  url = 'https://ria.ru/keyword_globalnoe_poteplenie/'
  global news_links
  news_links = []

  #отправка GET-запроса
  response = requests.get(url)


  #передаем текст ответа от сайта
  bs = BeautifulSoup(response.text,"lxml")

  
  temp = bs.find_all('a', 'list-item__title color-font-hover-only')

  for post in temp:
    news_links.append(post.text)
    news_links.append(post.get('href'))

  result_str = ''

  for str in news_links:
    result_str += str
    result_str += '\n'
    result_str += '\n'
  
  return result_str 

