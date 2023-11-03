import logging
from datetime import datetime
from bs4 import BeautifulSoup


from .crowler import Crowler
from .db import DB

logger = logging.getLogger('main')
categoris = ['rossiiskie-agronovosti',
             'mirovye-agronovosti',
             'zhivotnovodstvo',
             'selhoztehnika',
             'agroeconomics',
             'zhurnal-agroxxi',
             'monitoring-selskohozjaistvenyh-tovarov',]


class Agroxxi(Crowler):
    def __init__(self):
        self.BASE_URL = 'https://www.agroxxi.ru'
        self.URL = 'https://www.agroxxi.ru/novosti-selskogo-hozjaistva.html'

    def get_links(self, page):
        article_url = ''
        soup =  BeautifulSoup(page, "lxml")
        blocks = soup.find_all("div", class_="col-12 col-sm-8 pt-2 pt-lg-0")
        for block in blocks:
            a = block.find('a')
            article_url = str(a.get("href"))
            # print(f"[+] {text.strip()}  {url.strip()}")
            article_url = (self.BASE_URL + article_url.strip())
            logger.debug(f'article_url: {article_url}')
            db=DB()
            if not db.is_url_exists(article_url):
                yield article_url


    def get_article(self, url):# -> dict[str, Any]:# -> dict[str, Any]:
        datum = {}
        soup = BeautifulSoup(self.get_page(url), "lxml")
        article = soup.find("article")
        title = article.find('h1', class_='con_heading').text
        content = ''
        intro = ''
        all_p = article.find(
            "div", class_="articleBody con_text").find_all("p")
        datetime_str = article.find(
            "time", class_="con_pubdate col-12 col-sm-6 text-sm-end")['datetime'].strip()
        datetime_obj = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
        for p in all_p[:-2]:
            if all_p.index(p) == 0:
                intro += p.text.strip()
            else:
                content = content + p.text
        datum = {
                        'url':url, 
                        'domain_id':'2',  
                        'title':title,
                        'intro':intro, 
                        'content':content, 
                        'time':datetime_obj,
                        'category_id': 1,
                        }
        return datum

       
