from django.db import models
import uuid

# Create your models here.
class Party(models.Model):
    number_party = models.IntegerField(verbose_name='Номер отряда')
    name = models.CharField(verbose_name='Название отряда', max_length=255)
    token_qr = models.CharField(verbose_name='Номер qr', max_length=255, default=uuid.uuid4())
    money = models.IntegerField(verbose_name='Деньги', default=0)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Отряд'
        verbose_name_plural = 'Отряд'