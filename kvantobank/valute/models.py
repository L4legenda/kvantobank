from django.db import models

# Create your models here.
class Valute(models.Model):
    name = models.CharField(verbose_name="Название", max_length=255)
    attitude = models.IntegerField(verbose_name="1 коин/руб")
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Валюта"
        verbose_name_plural = "Валюта"

class Tranzaction(models.Model):
    valute = models.ForeignKey(Valute, on_delete=models.DO_NOTHING)
    count = models.IntegerField()