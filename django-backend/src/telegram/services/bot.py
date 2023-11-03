
import logging
import time
from django.conf import settings
import telebot
from scrapper.models import Article
from scrapper.services.db import DB
from random import randint



logger = logging.getLogger('main')


channals = {'1' :settings.ID_CHANNAL_APK}

class tgBot():
    
    def run(self):
        bot = telebot.TeleBot(settings.TOKEN,parse_mode='HTML')
        unpublised = Article.objects.get(is_published=False)
        db = DB()
        news = f'<b>{unpublised.title}</b>\n\n{unpublised.summary}\n\n\n<a href="{unpublised.url}">Читать источник</a>'
        categoty_id = str(unpublised.category_id)
        bot.send_message(channals[categoty_id],news)
        db.set_published(unpublised)