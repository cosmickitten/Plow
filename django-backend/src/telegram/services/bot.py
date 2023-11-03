
import logging
import time
from django.conf import settings
import telebot
from scrapper.models import Article
from scrapper.services.db import DB
from random import randint



logger = logging.getLogger('main')




class tgBot():
    def __init__(self) -> None:
        self.channals = {'1' :settings.ID_CHANNAL_APK}
        self.TOKEN = '6743554482:AAHLzpjEdO49BTjsxm5SS3uviYIrRBm5bng'
    
    def run(self):
        
        bot = telebot.TeleBot(self.TOKEN,parse_mode='HTML')
        unpublised = Article.objects.filter(is_published=False).filter(is_summarized = True)
        if len(unpublised) > 0:
            article = unpublised[0]
            db = DB()
            news = f'<b>{article.title}</b>\n\n{article.summary}\n\n\n<a href="{article.url}">Читать источник</a>'
            category_id = str(article.category_id)
            bot.send_message('599272752',news)
            
            db.set_published(article)