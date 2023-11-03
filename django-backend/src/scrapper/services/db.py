import logging
from django.db import IntegrityError
from django.db.utils import OperationalError

from scrapper.models import Article, Domain, Category


from .utils import  Utils

from llm.services.summary import AI
from llm.services.summary2 import  AI2


logger = logging.getLogger('main')

utility = Utils()


class DB():

    def save_(self, url, domain_id, title, intro, content,time,category_id):

        logger.debug(
            f'url= {url}, site = {url}, time = {str(time)}')
        

        a = Article(title=title, intro=intro, content=content,is_summarized = False, time=time, url=url,category_id = category_id,domain_id=domain_id)
        #article_text = a.intro + a.content
        

        try:
            a.save()
            utility.count_queries(insert = 1,records = 1)

            logger.info(
                f'Успешно! url= {url}')

        except IntegrityError as e:
            logger.error(f'Database error! {e} caused {url} ')

            # except OperationalError as e:
            #    logger.error(f'Закрой базу данных дебил!! ')


    def is_url_exists(self, url):
        try:
            Article.objects.get(url=url)
            utility.count_queries(select=1)
            return True
        except Article.DoesNotExist:
            return False
        
    def set_published(self, obj):
        obj.is_published = True
        obj.save()
