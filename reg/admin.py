from django.contrib import admin
from .models import reg
#регистрация таблиц из баз данных
# Register your models here.

#Добавляем таблицу из models.py
admin.site.register(reg)

'''class NewFileAdmin(admin.ModelAdmin):
    exclude = ('Responsible', )

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.Responsible = request.user
        super().save_model(request, obj, form, change)'''