# Generated by Django 4.2.7 on 2023-11-02 22:01

from django.db import migrations

def add_domains(apps, schema_editor):
    Domain = apps.get_model('scrapper', 'Domain')
    Domain.objects.create(name = 'https://agrovesti.net')
    Domain.objects.create(name = 'https://www.agroxxi.ru')
    Domain.objects.create(name = 'https://1prime.ru')
    Domain.objects.create(name = 'https://agri-news.ru')
    Domain.objects.create(name = 'https://rg.ru')





def add_category(apps, schema_editor):
    Category = apps.get_model('scrapper', 'Category')
    Category.objects.create(name = 'АПК')
   
class Migration(migrations.Migration):

    dependencies = [
        ('scrapper', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_domains),
        migrations.RunPython(add_category),
    ]
