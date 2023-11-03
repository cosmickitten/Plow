from datetime import datetime
import logging
from bs4 import BeautifulSoup
from .crowler import Crowler
from .db import DB



logger = logging.getLogger('main')


class Prime(Crowler):
    def __init__(self):
        self.BASE_URL = 'https://1prime.ru'
        self.URL = 'https://1prime.ru/Agriculture/'

    def get_links(self, page):
        article_url = ''
        soup = BeautifulSoup(page, "lxml")
        all_h = soup.find_all('h2', class_='rubric-list__article-title')
        for block in all_h:
            a = block.find('a')
            article_url = str(a.get("href"))
            article_url = (self.BASE_URL + article_url.strip())
            logger.debug(f'article_url: {article_url}')
            db=DB()
            if not db.is_url_exists(article_url):
                yield article_url

    
    def get_article(self, url):
        datum = {}
        soup = BeautifulSoup(self.get_page(url), "lxml")
        article = soup.find("article", class_="article")
        title = article.find("div", class_="article-header").find(
            "header").find('div', class_="article-header__title").text
        body = article.find("div", class_="article-body__content")
        intro = ''
        content = ''
        all_p = body.find_all("p")
        datetime_str = soup.find("div", class_="layout__date").find('span')[
            'data-unix'].strip()
        datetime_obj = datetime.utcfromtimestamp(
            int(datetime_str)).strftime('%Y-%m-%d %H:%M:%S')

        for p in all_p:
            if all_p.index(p) == 0:
                intro += p.text.strip()
            else:
                content = content + p.text
        index = intro.find('.')
        intro = intro[index+2::]

        
        datum = {
                        'url':url, 
                        'domain_id':'3',  
                        'title':title,
                        'intro':intro, 
                        'content':content, 
                        'time':datetime_obj,
                        'category_id': 1,
                        }
        return datum

