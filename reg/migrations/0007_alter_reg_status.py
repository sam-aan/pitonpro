# Generated by Django 4.1 on 2022-08-28 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0006_alter_reg_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reg',
            name='Status',
            field=models.CharField(choices=[('создан', 'создан'), ('зарегистрирован', 'зарегистрирован'), ('согласован', 'согласован'), ('завершен', 'завершен')], default='создан', max_length=30, verbose_name='Статус'),
        ),
    ]
