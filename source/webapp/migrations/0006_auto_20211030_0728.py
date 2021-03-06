# Generated by Django 3.2 on 2021-10-30 07:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0005_auto_20211028_0740'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='technique',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='technique',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='technique',
            name='start_time',
        ),
        migrations.AlterField(
            model_name='technique',
            name='qty',
            field=models.PositiveIntegerField(verbose_name='Количество часов со скидкой'),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(blank=True, null=True, verbose_name='Время начало')),
                ('end_time', models.DateTimeField(blank=True, null=True, verbose_name='Время конца')),
                ('description', models.TextField(max_length=3000, verbose_name='Описание')),
                ('offered_price', models.DecimalField(decimal_places=0, max_digits=7, verbose_name='Предлагаемая цена')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
        ),
    ]
