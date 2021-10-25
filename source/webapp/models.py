from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
import phonenumbers


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name="Категория")

    def __str__(self):
        return f"{self.pk} - {self.name}"


class Technique(models.Model):
    price_choices =[("hour", "час"), ("flight", "рейс"), ("km", "км"), ("cub.m.", "куб.м."), ("kg", "кг")]
    status_choices =[("free", "свободен"), ("busy", "занят")]

    category = models.ForeignKey("webapp.Category", on_delete=models.CASCADE, verbose_name="Категория", related_name="Техника")
    name = models.CharField(max_length=150, verbose_name="Наименование")
    foto = models.ImageField(null=True, blank=True, upload_to='user_pics', verbose_name="Фото техники")
    price = models.DecimalField(max_digits=7, decimal_places=0, verbose_name="Стоимость услуги")
    price_description = models.CharField(max_length=50, choices=price_choices, default="hour", verbose_name="Описание стоимости")
    description = models.TextField(max_length=3000, verbose_name="Описание")
    phone_number = PhoneNumberField(unique=True, verbose_name="Контактный телефон")
    start_time = models.DateTimeField(null=True, blank=True, verbose_name="Время начало")
    end_time = models.DateTimeField(null=True, blank=True, verbose_name="Время конца")
    status = models.CharField(max_length=30, choices=status_choices, default="free", verbose_name="Статус")
    qty = models.PositiveIntegerField(verbose_name="Количество")
    sale_price = models.DecimalField(max_digits=7, decimal_places=0, verbose_name="Стоимость услуги со скидкой")
    is_active = models.BooleanField(default=True, verbose_name="Активный")

    def __str__(self):
        return f"{self.pk} - {self.category.name}"


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    text = models.TextField(max_length=3000, verbose_name="Комментарий")

    def __str__(self):
        return f"{self.pk} - {self.author}"