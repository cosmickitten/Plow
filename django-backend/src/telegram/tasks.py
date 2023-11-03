from celery import shared_task
from telegram.services.bot import tgBot


@shared_task
def task_telegram():
    bot = tgBot()
    bot.run()
