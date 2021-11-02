from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name="Категория")
    title = models.CharField(max_length=150, verbose_name="Наименование")

    def __str__(self):
        return self.title


class Technique(models.Model):
    price_choices =[("час", "час"), ("рейс", "рейс"), ("км", "км"), ("куб.м.", "куб.м."), ("кг", "кг")]
    status_choices =[("свободен", "свободен"), ("занят", "занят")]

    advertiser = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор объявления", related_name="techniques")
    category = models.ForeignKey("webapp.Category", on_delete=models.CASCADE, verbose_name="Категория", related_name="Техника")
    name = models.CharField(max_length=150, verbose_name="Наименование")
    foto = models.ImageField(null=True, blank=True, upload_to='user_pics', verbose_name="Фото техники")
    price = models.DecimalField(max_digits=7, decimal_places=0, verbose_name="Стоимость услуги")
    price_description = models.CharField(max_length=50, choices=price_choices, default="час", verbose_name="Описание стоимости")
    description = models.TextField(max_length=3000, verbose_name="Описание")
    status = models.CharField(max_length=30, choices=status_choices, default="свободен", verbose_name="Статус")
    qty = models.PositiveIntegerField(verbose_name="Количество часов со скидкой")
    sale_price = models.DecimalField(max_digits=7, decimal_places=0, verbose_name="Стоимость услуги со скидкой")
    is_active = models.BooleanField(default=True, verbose_name="Активный")

    def __str__(self):
        return f"{self.pk} - {self.category.name}"


class Order(models.Model):
    technique = models.ForeignKey("webapp.Technique", on_delete=models.CASCADE,
                                  verbose_name="Заявка на технику", related_name="orders")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    start_time = models.DateTimeField(null=True, blank=True, verbose_name="Время начало")
    end_time = models.DateTimeField(null=True, blank=True, verbose_name="Время конца")
    description = models.TextField(max_length=3000, verbose_name="Описание")
    offered_price = models.DecimalField(max_digits=7, decimal_places=0, verbose_name="Предлагаемая цена")


class Comment(models.Model):
    technique = models.ForeignKey("webapp.Technique", on_delete=models.CASCADE,
                                  verbose_name="Комментарий на технику", related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    text = models.TextField(max_length=3000, verbose_name="Комментарий")

    def __str__(self):
        return f"{self.pk} - {self.author}"