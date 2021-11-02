# Generated by Django 3.2 on 2021-10-30 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_auto_20211030_0732'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='technique',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='webapp.technique', verbose_name='Заявка на технику'),
            preserve_default=False,
        ),
    ]
