from django.db import models

class MedicalProduct(models.Model):
    name = models.CharField(max_length=255)
    image = models.URLField()
    price = models.IntegerField(default=100)

    def __str__(self):
        return self.name
