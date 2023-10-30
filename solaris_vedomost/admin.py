from django.contrib import admin
from .models import SolVed
from .models import IP
from .models import Seria
from .models import detal
#регистрация таблиц из баз данных
# Register your models here.

#Добавляем таблицу из models.py
admin.site.register(SolVed)
admin.site.register(IP)
admin.site.register(Seria)
admin.site.register(detal)
