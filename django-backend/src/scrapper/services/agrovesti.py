import logging
from datetime import datetime
from bs4 import BeautifulSoup
from .db import DB
from .crowler import Crowler



logger = logging.getLogger('main')


class Agrovesti(Crowler):
    def __init__(self):

        self.BASE_URL = 'https://agrovesti.net'
        self.URL_CORP = 'https://agrovesti.net/news/corp.html'
        self.URL_NEWS = 'https://agrovesti.net/news/indst.html'
        self.LINKS = {self.URL_CORP: 'corp', self.URL_NEWS: 'indst'}

    def get_links(self, page, tag):

        article_url = ''
        soup = BeautifulSoup(page, "lxml")
        page_all_a = soup.find_all("a")
        for i in page_all_a:
            article_url = str(i.get("href"))

            try:
                if (article_url.split('/')[1] == 'news') and (article_url.split('/')[2] == tag) and (article_url.split('/')[3][0:5] != "page-"):
                    # print(f"[+] {text.strip()}  {url.strip()}")
                    article_url = (self.BASE_URL + article_url.strip())
                    logger.debug(f'article_url: {article_url}')
                    db=DB()
                    if not db.is_url_exists(article_url):
                        yield article_url
            except:
                IndexError

    
    def get_article(self, url):
        datum = {}
        soup =  BeautifulSoup(self.get_page(url), "lxml")
        article = soup.find("div",  class_="article-main")
        datetime_str = article.find(
            "dd", class_="date-published").find("time")['datetime'].strip()
        # datetime = '2023-09-29 07:58:38'

        datetime_obj = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')

        title = article.find("h1",  class_="article-title").text.strip()
        intro = article.find(
            "div", class_="article-intro").find("p").text.strip()
        # удаление блока с соцсетями
        content = article.find("div", class_="article-full").text[:-51]

       
        datum = {
                        'url':url, 
                        'domain_id':'1', 
                        'title':title,
                        'intro':intro, 
                        'content':content, 
                        'time':datetime_obj,
                        'category_id': 1,
                        }
        return datum


   
    def start(self):
        logger.info(f"Старт парсера {self.get_sitename(self.BASE_URL)}")
        for url in self.LINKS:
            page = self.get_page(url)
            for url in self.get_links(page, self.LINKS[url]):
                data = self.get_article(url)
                db = DB()
                db.save_(**data)
