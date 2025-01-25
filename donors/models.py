from django.db import models

# Create your models here.
class DONOR(models.Model):
    name = models.CharField(max_length = 200)
    party = models.CharField(max_length = 200)

    def __str__(self):
        return self.name
