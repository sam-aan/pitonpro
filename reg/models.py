from django.db import models


class reg(models.Model):
    class Stat(models.Model):
        STATUS = (
            ('создан', 'создан'),
            ('в работе', 'в работе'),
            ('согласован', 'согласован'),
            ('завершен', 'завершен')
        )

    numbers = models.CharField('Номер проекта', max_length=10)
    NameProg = models.CharField('Наименование', max_length=100)
    Date_born = models.DateField('Дата создания', auto_now=True)
    Responsible = models.CharField('Отвественный', max_length=100)
    Customer_company = models.CharField('', max_length=50)
    Adres_obj = models.TextField('Адрес объекта')
    Status = models.CharField('Статус', max_length=30, default='создан', choices=Stat.STATUS)

    # название строчки в таблице
    def __str__(self):
        return 'Проект №' + self.numbers + ' ' + self.NameProg

    # название таблицы
    class Meta:
        verbose_name = 'Таблица регистрации'
