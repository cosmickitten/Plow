"""Модуль предоставляет базовый класс парсера."""
import requests
import logging
from .db import DB

logger = logging.getLogger('main')


class Crowler():
    """Базовый класс парсера"""

    def __init__(self) -> None:
        self.URL: str
        self.BASE_URL: str

    def get_links(self, page):
        """Метод для выделения ссылок с страницы возвращает генератор"""
        pass

    def get_article(self, url)-> dict:
        """Метод принимает страницу с новостью и выдает словарь для БД"""
        return {}

    def get_page(self, url):
        """Загрузка html страницы для дальнейщего разбора"""
        headers = {
            "Accept": "application/json",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0",
        }
        try:
            r = requests.get(url, headers=headers, timeout=10)
            if r.status_code == 200:
                src = r.text
            else:
                logger.error(f"Ошибка сети {r.status_code}")
            return (src)
        except requests.exceptions.ReadTimeout:
            i = 0
            while i < 5:
                self.get_page(url)
                i += 1

    def get_sitename(self, url):
        """Получение названия сайта из url"""
        return url.split('//')[-1].split('.')[-2]

    def start(self):
        """Главная функция запуска парсеров"""
        logger.info(f"Старт парсера {self.get_sitename(self.BASE_URL)}")
        page = self.get_page(self.URL)
        for article_url in self.get_links(page):
            data = self.get_article(article_url)
            db = DB()
            db.save_(**data)
            
