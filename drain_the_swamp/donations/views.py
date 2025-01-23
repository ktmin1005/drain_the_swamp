from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

class Donations(models.Model):
    president = models.ForeignKey('presidents.President', on_delete = models.CASCADE, related_name = 'donation')
    donor_name = models.CharField(max_length = 100)
    amount = models.DecimalField(max_digits = 12, decimal_places = 2)
    date = models.DateField()
    source = models.URLField(blank = True, null = True)

    def __str__(self):
        return f"{self.donor_name} donated ${self.amount} to {self.president.name}"