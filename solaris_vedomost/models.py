from django.db import models
from reg.models import reg

class SolVed(models.Model):

    class Prom(models.Model):
        PROM = (
            ('Питон кама', 'Питон кама'),
            ('Солярис', 'Солярис')
        )
    class Stat(models.Model):
        STATUS = (
            ('создан', 'создан'),
            ('в работе', 'в работе'),
            ('на упаковке', 'на упаковке'),
            ('отгружен', 'отгружен'),
            ('завершён', 'завершён')
        )

    NomZak = models.CharField('Номер заказа', max_length=15)
    NomProj = models.ForeignKey(reg, db_index=True, max_length=100, on_delete=models.PROTECT, null=True)
    Date_creation = models.DateField('Дата создания', auto_now=True)
    Responsible = models.CharField('Отвественный', max_length=100)
    PromPlosh = models.CharField('Производственная площадка', default='Солярис', max_length=30, choices=Prom.PROM)
    Status = models.CharField('Статус', max_length=15, default='создан', choices=Stat.STATUS)
    uploadedFile = models.FileField(upload_to="Uploaded Files/", null=True)

    # название строчки в таблице
    def __str__(self):
        return 'Номер заказа: ' + self.NomZak

    # название таблицы
    class Meta:
        verbose_name = 'Таблица Заказов'

class IP(models.Model):

    Ip = models.CharField('Степень защиты оболочки', max_length=2)

    # название строчки в таблице
    def __str__(self):
        return 'IP ' + self.Ip
    # название таблицы
    class Meta:
        verbose_name = 'IP'

class Seria(models.Model):

    Ser = models.CharField('Наименование серии', max_length=15)
    Ip = models.ForeignKey(IP, db_index=True, max_length=2, on_delete=models.PROTECT)
    Matprov = models.CharField('Материал проводника', max_length=15)
    Kolprov = models.CharField('Количество проводников', max_length=15)
    Nomprov = models.CharField('Номинальный ток проводника', max_length=15)

    # название строчки в таблице
    def __str__(self):
        return 'Серия' + self.Ser + self.Matprov + ' Кол.пров ' + self.Kolprov
    # название таблицы
    class Meta:
        verbose_name = 'Серия'

class detal(models.Model):

    Name = models.CharField('Наименование', max_length=30)
    Nomer = models.CharField('Обозначение', max_length=15)
    Weight = models.DecimalField('Масса', max_digits=5, decimal_places=3)

    # название строчки в таблице
    def __str__(self):
        return self.Nomer + self.Name

    # название таблицы
    class Meta:
        verbose_name = 'Деталь'