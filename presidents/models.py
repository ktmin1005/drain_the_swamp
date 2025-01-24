import datetime
from django.db import models
from django.utils import timezone


# Create your models here.
class President(models.Model):
    name = models.CharField(max_length = 100) # president's name
    term_start = models.DateField() # start year of the presidency
    term_end = models.DateField() # end year of the presidency
    party = models.CharField(max_length = 50) # president's party

    def __str__(self):
        return f"{self.name} ({self.party}) served from {self.term_start} to {self.term_end}."
    
    def is_incumbent(self):
        now = timezone.now().date()
        return self.term_start <= now <= self.term_end

"""
class Donor(models.Model):
    name = models.CharField(max_length = 100) # name of the donor
    organization = models.CharField(max_length = 100, blank = True, null = True) # org the donor belongs to (optional)
    industry = models.CharField(max_length = 100, blank = True, null = True) # industry of the org (optional)
    
    def __str__(self):
        return self.name
    
class Donation(models.Model):
    president = models.ForeignKey(President, on_delete = models.CASCADE, related_name = 'donations') # related_name means the name for the reverse relationship
    donor = models.ForeignKey(Donor, on_delete = models.CASCADE, related_name = 'donations')
    amount = models.DecimalField(max_digits = 15, decimal_places = 2) # donation amount

    def __str__(self):
        return f"{self.donor.name} donated ${self.amount} to {self.president.name} under the name of the organization {self.donor.organization} in the industry {self.donor.industry}."

class Policy(models.Model):
    name = models.CharField(max_length = 200) # policy name
    description = models.TextField() # policy description
    endorsed_by = models.ManyToManyField(President, related_name = 'endorsed_policies', blank = True) # endorsing presidents
    opposed_by = models.ManyToManyField(President, related_name = 'opposed_policies', blank = True) # opposing presidents

    def __str__(self):
        return self.name

class LegislativeAction(models.Model):
    ACTION_CHOICE = [
        ('ENACTED', 'enacted'),
        ('VETOED', 'vetoed'),
        ('NOT_ENACTED', 'did not enact'),
    ]

    president = models.ForeignKey(President, on_delete = models.CASCADE, related_name = 'actions')
    policy = models.ForeignKey(Policy, on_delete = models.CASCADE, related_name = 'actions')
    action = models.CharField(max_length = 20, choices = ACTION_CHOICE)
    date = models.DateField()

    def __str__(self):
        return f"{self.president.name} {self.action} {self.policy.name}"


OR IN THE CASE I USE MULTIPLE APPS TO SEPERATE PRESIDENTS, DONATIONS, AND POLICIES:
class Donation(models.Model):
    donor_name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    president = models.ForeignKey(
        'presidents.President', 
        on_delete=models.CASCADE, 
        related_name='donations'
    )
    date = models.DateField()

class Policy(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(
        max_length=10,
        choices=[
            ('endorsed', 'Endorsed'),
            ('opposed', 'Opposed'),
            ('enacted', 'Enacted'),
            ('vetoed', 'Vetoed'),
        ]
    )
    president = models.ForeignKey(
        'presidents.President', 
        on_delete=models.CASCADE, 
        related_name='policies'
    )
"""    
