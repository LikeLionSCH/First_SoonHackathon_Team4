from django.db import models

class Product(modles.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to = "product/", black=True, null=True)

    def __str__(self):
        return self.title