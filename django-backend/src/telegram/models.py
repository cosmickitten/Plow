from django.db import models

# Create your models here.
class Channel(models.Model):
    channal = models.CharField(max_length=255, blank=False,
                            null=False, verbose_name='Channal ID')
    

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Канал'
        verbose_name_plural = 'Каналы'


#class Settings(models.Model):
#    bot_token = models.CharField(max_length=255, blank=False,
#                            null=False, verbose_name='TOKEN')
    
