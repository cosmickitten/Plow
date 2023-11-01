
import logging
import time
from django.conf import settings
#import telebot
#from plaugh_service.models import Article
#from plaugh_service.scrapper.db import DB
#from random import randint



# logger = logging.getLogger('main')


# channals = {'1' :settings.ID_CHANNAL_APK}

# class tgBot():
    
#     def start(self):
#         bot = telebot.TeleBot(settings.TOKEN,parse_mode='HTML')
#         unpublised = Article.objects.filter(is_published=False)

#         for num, a in enumerate(unpublised, 1):
#             db = DB()
#             news = f'<b>{a.title}</b>\n\n{a.summary}\n\n\n<a href="{a.url}">Читать источник</a>'
#             categoty_id = str(a.category_id)
#             bot.send_message(channals[categoty_id],news)
#             logger.info(f'Опубликовано:{num} из {len(unpublised)} {a.url}')
#             if len(unpublised) > 1:
#                 time.sleep(randint(60,300))
#             db.set_published(a)