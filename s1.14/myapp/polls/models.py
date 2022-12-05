from django.db import models


class Shop(models.Model):
    title = models.CharField(max_length=200)
    email = models.EmailField()
    created_date = models.DateTimeField('created_at')

    def __str__(self):
        return self.title


class Product(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200, null=True, blank=True)
    price = models.PositiveIntegerField()
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.title
