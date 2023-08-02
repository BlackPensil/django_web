# Create your models here.
# Advertisement:
# title
# description
# price
# auction
# created_at
# updated_at
from django.db import models
from django.contrib import admin
class Advertisements(models.Model):

    title = models.CharField(
        max_length=100,
        verbose_name='Название',
    )

    description = models.TextField(
        verbose_name='Описание'
    )

    price = models.DecimalField(
        verbose_name='Цена',
        max_digits=10,
        decimal_places=2
    )

    auction = models.BooleanField(
        verbose_name='Торг',
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации'
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата редактирования'
    )

    @admin.display(description='Дата создания')
    def created_date(self):
        from django.utils import timezone
        from django.utils.html import format_html

        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color: green; font-weight: bold;">Сегодня в {}</span>', created_time
            )
        return self.created_at.strftime('%d.%m.%Y в %H:%M:%S')

    def __str__(self):
        return f'id={self.id}, title={self.title}, description={self.description}, price={self.price}'



