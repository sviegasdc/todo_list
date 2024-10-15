from django.db import models


# Create your models here.
class Lista(models.Model):
    item = models.CharField(max_length=100, unique=True)
    id_item = models.AutoField(primary_key=True)

    def __str__(self):
        return self.item
