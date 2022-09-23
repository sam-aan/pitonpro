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
        return 'Номер заказа: ' + self.NomZak + ' Статус: ' + self.Status

    # название таблицы
    class Meta:
        verbose_name = 'Таблица Заказов'
