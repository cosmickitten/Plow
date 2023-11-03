import locale
import logging
from datetime import datetime
from bs4 import BeautifulSoup

from .db import DB
from .crowler import Crowler



logger = logging.getLogger('main')


class Agrinews(Crowler):
    def __init__(self):
        self.BASE_URL = 'https://agri-news.ru'
        self.URL = 'https://agri-news.ru/novosti/'

    def convert_date(self, datetime_str):
        locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
        datetime_str = datetime_str.split(' ')
        month = {'января': 'January',
                 'февраля': 'February',
                 'мартa': 'March',
                 'апреля': 'April',
                 'мая': 'May',
                 'июня': 'June',
                 'июля': 'July',
                 'августа': 'August',
                 'сентября': 'September',
                 'октября': 'October',
                 'ноября': 'November',
                 'декабря': 'December'
                 }
        

        for key, value in month.items():
            if datetime_str[1].strip() == key:
                datetime_str[1] = value
        datetime_str = ' '.join(str(x) for x in datetime_str)
        datetime_obj = datetime.strptime(datetime_str, "%d %B %Y")
        return datetime_obj

    def get_links(self, page):
        db = DB()
        soup = BeautifulSoup(page, "lxml")
        main = soup.find("div", class_="col col_9_of_12 main_content")
        blocks = main.find_all("div", class_="item_content")
        for block in blocks:
            a = block.find_next("h2").find_next('a')
            article_url = str(a.get("href"))
            article_url = (self.BASE_URL + article_url.strip())
            logger.debug(f'article_url: {article_url}')
            if not db.is_url_exists(article_url):
                yield article_url

   
    def get_article(self, url):
        datum = {}
        soup = BeautifulSoup(self.get_page(url), "lxml")
        article = soup.find("article", class_="single_post")
        title = article.find(
            "header", class_="post_header").find_next('h1').text
        body = article.find("div", class_="post_content")
        intro = ''
        content = ''
        all_p = body.find_all("p")
        datetime_str = article.find("span", class_="date")["datetime"]
        datetime_obj = self.convert_date(datetime_str)
        for p in all_p:
            content = content + p.text

        
        datum = {
                        'url':url, 
                        'domain_id':'4',  
                        'title':title,
                        'intro':intro, 
                        'content':content, 
                        'time':datetime_obj,
                        'category_id': 1
                        }
        return datum

