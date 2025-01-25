from django.db import models
from django.utils import timezone
import datetime
# Create your models here.

class Candidate(models.Model):
    name = models.CharField(max_length = 100)
    party = models.CharField(max_length = 100)
    position = models.CharField(max_length = 100)
    term_start = models.DateField()
    term_end = models.DateField()
    incumbent = models.BooleanField(default = False)

    def __str__(self):
        return f"{self.name}, a ({self.party}) served as a {self.position} from {self.term_start} to {self.term_end}."
    
    def save(self, *args, **kwargs):
        self.incumbent = self.term_end is None or self.term_end > timezone.now().date
        super().save(*args, **kwargs)

    def is_incumbent(self):
        return f"{self.name} ({'Incumbent' if self.incumbent else 'Former'})"

class Campaign(models.Model):
    name = models.CharField(max_length = 200)
    description = models.TextField()
    year = models.PositiveIntegerField()
    funds_raised = models.DecimalField(max_digits = 15, decimal_places = 2, default = 0.0)

    def __str__(self):
        return f"{self.candidate.name} - Campaign {self.year}"