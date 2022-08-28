from django.db import models
from django.shortcuts import render, redirect

class reg(models.Model):

    nombers = models.CharField('Номер проекта', max_length=10)
    NameProg = models.CharField('Наименование', max_length=100)
    Date_born = models.DateField('Дата создания', auto_now=True)
    Responsible = models.CharField('Отвественный', max_length=100)
    Customer_company = models.IntegerField('Организация заказчик ИНН', max_length=10)
    Adres_obj = models.TextField('Адрес объекта')
    Status = models.CharField('Статус', max_length=15, default='создан')

    # название строчки в таблице
    def __str__(self):
        return 'Проект №' + self.nombers + ' ' + self.NameProg + ' Статус: ' + self.Status

    # название таблицы
    class Meta:
        verbose_name = 'Таблица регистрации'
