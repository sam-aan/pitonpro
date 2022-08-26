from django.contrib import admin
from .models import reg
#регистрация таблиц из баз данных
# Register your models here.

#Добавляем таблицу из models.py
admin.site.register(reg)