import datetime
from django.db import models
from django.utils import timezone


# Create your models here.
class President(models.Model):
    name = models.CharField(max_length = 100) # president's name
    term_start = models.DateField() # start year of the presidency
    term_end = models.DateField() # end year of the presidency
    party = models.CharField(max_length = 50) # president's party
    incumbent = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} ({self.party}) served from {self.term_start} to {self.term_end}."
    
    def save(self, *args, **kwargs):
        self.incumbent = self.term_end is None or self.term_end > timezone.now().date()


    def is_incumbent(self):
        return f"{self.name} ({'Incumbnent' if self.incumbent else 'Former'})"
