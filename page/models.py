from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name='Категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категория'


class Logo(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    name = models.CharField(max_length=250, verbose_name='Наименование')
    logo = models.FileField(verbose_name="Логотип", upload_to='logo')
    url = models.URLField(verbose_name='Ссылка')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Объект'
        verbose_name = 'Объект'


