from django.db import models


class Category(models.Model):
    name = models.CharField('Название', max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField('Название', max_length=50)
    price = models.IntegerField('Цена')
    description = models.CharField('Описание', max_length=1000)
    imgs = models.ManyToManyField('Image')
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE, default='CAT')

    def __str__(self):
        return self.name


class Image(models.Model):
    name = models.CharField('Название', max_length=50)
    src = models.ImageField('Путь', upload_to='images/')

    def __str__(self):
        return self.name
