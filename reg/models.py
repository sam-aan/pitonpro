from django.db import models

class reg(models.Model):
    nombers = models.CharField('Номер проекта', max_length=10)
    Date = models.DateField('Дата', auto_now=True)
    NameProg = models.CharField('Наименование', max_length=100)
    Status = models.CharField('Статус', max_length=15)

    # название строчки в таблице
    def __str__(self):
        return 'Прокт №' + self.nombers + ' ' + self.NameProg + ' Статус: ' + self.Status

    # название таблицы
    class Meta:
        verbose_name = 'Таблица регистрации'
