from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to = "product/", blank=True, null=True)

    def __str__(self):
        return self.title