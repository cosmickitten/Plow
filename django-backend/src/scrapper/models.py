from django.db import models

# Create your models here.

class Article(models.Model):
    class Published(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        READY = 1, 'Опубликовано'

    class Banned(models.IntegerChoices):
        NO = 0, 'Нет'
        YES = 1, 'Да'

    class Summarized(models.IntegerChoices):
        NO = 0, 'Нет'
        YES = 1, 'Да'


    title = models.CharField(max_length=255, verbose_name='Заголовок')
    intro = models.TextField(verbose_name='Кратко')
    content = models.TextField(verbose_name='Текст статьи')
    time = models.DateTimeField(verbose_name='Опубликовано')
    time_add = models.DateTimeField(
        auto_now_add=True, verbose_name='Добавлено')
    url = models.URLField(null=False, blank=False,max_length=200, unique=True,verbose_name='Ссылка')
    summary = models.TextField( null=True, blank=True, verbose_name='Генерат')
    is_published = models.BooleanField(choices=Published.choices,default=Published.DRAFT,verbose_name='Статус')
    is_banned = models.BooleanField(choices=Banned.choices,default=Banned.NO,verbose_name='Готово к публикации')
    is_summarized = models.BooleanField(choices=Summarized.choices,default=Summarized.NO,verbose_name='Забанено')
    domain = models.ForeignKey('Domain',  on_delete=models.SET_NULL, null=True, related_name='article',verbose_name='Caйт')
    category = models.ForeignKey('Category',on_delete=models.SET_NULL, null=True, related_name='url')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-time']
        indexes = [
            models.Index(fields=['-time']),
        ]


class Domain(models.Model):
    name = models.URLField(max_length=20, verbose_name='Сайт',unique=True)
   

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Сайт'
        verbose_name_plural = 'Сайты'
        indexes = [
            models.Index(fields=['name']),
        ]




class Category(models.Model):
    name = models.CharField(max_length=255, blank=False,
                            null=False, verbose_name='Категория')
    telegram_id_channal = models.OneToOneField('telegram.Channel',on_delete=models.SET_NULL, null=True, related_name='category')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
