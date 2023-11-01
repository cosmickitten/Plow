from datetime import datetime
import logging
from bs4 import BeautifulSoup
import re
from .crowler import Crowler
from .db import DB





logger = logging.getLogger('main')


class RG(Crowler):
    def __init__(self):
        self.BASE_URL = 'https://rg.ru'
        self.URL = 'https://rg.ru/tema/ekonomika/apk'


    def get_links(self, page):
        article_url = ''
        soup = BeautifulSoup(page, "lxml")
        all_div = soup.find_all('div', class_=re.compile("PageRubricContent_listItem"))
        for block in all_div:
            a = block.find('a')
            article_url = str(a.get("href"))
            article_url = (self.BASE_URL + article_url.strip())
            logger.debug(f'article_url: {article_url}')
            db=DB()
            if not db.is_url_exists(article_url):
                yield article_url


    def get_article(self, url):# -> dict[str, Any]:# -> dict[str, Any]:
        datum = {}
        content = ''
        soup = BeautifulSoup(self.get_page(url), "lxml")
        article = soup.find("div", class_=re.compile('Page_main'))
        if article is None:
            article = soup.find("main", class_=re.compile('PageArticle_main'))
            title = article.find('h1', class_=re.compile('PageArticleTitle_title')).text
            datetime_str = article.find("span", class_=re.compile("PageArticleTitle_day")).string
            intro = article.find('h3', class_=re.compile('PageArticleTitle_lead')).text
            text_block = article.find('article', class_=re.compile('PageArticleContent_article'))
            all_p = text_block.find_all("p")
            datetime_obj = datetime.strptime(datetime_str, '%d.%m.%Y')
            for p in all_p:
                content = content + p.text
        else:

            #print(article)
            title = article.find('h1', class_=re.compile('PageArticleContent_title')).text            
            intro = article.find('div', class_=re.compile('PageArticleContent_lead')).text
            all_p = article.find(
                "div", class_=re.compile('PageArticleContent_content')).find_all("p")
            datetime_str = article.find(
                "div", class_=re.compile("PageArticleContent_date_")).string
            datetime_obj = datetime.strptime(datetime_str, '%d.%m.%Y %H:%M')
            for p in all_p:
                content = content + p.text
        datum = {
                        'url':url, 
                        'domain_id': '5',  
                        'title':title,
                        'intro':intro, 
                        'content':content, 
                        'article_text' : title + intro + content,
                        'time':datetime_obj,
                        'category_id': 1,
                        }
        return datum
