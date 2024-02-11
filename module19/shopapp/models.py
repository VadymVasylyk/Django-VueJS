from django.db import models

class Item (models.Model):
    slug = models.SlugField('Slug', unique=True)
    title = models.CharField('Title', max_length=200)
    image = models.CharField('Image', max_length=50)
    desc = models.TextField('Description')
    price = models.DecimalField('Prise', max_digits=5, decimal_places=2)

    def __str__(self):
        return self.title