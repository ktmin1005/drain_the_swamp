from django.db import models
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
#from donors.models import DONOR


# Create your models here.
class Donation(models.Model):
#    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    recipient_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    recipient_object_id = models.PositiveIntegerField()
    recipient = GenericForeignKey('recipient_content_type', 'recipient_object_id')
    amount = models.DecimalField(max_digits = 10, decimal_places = 2)
    date = models.DateField()

#    def __str__(self):
#        return f"{self.donor_name} donated ${self.amount} to {self.president.name}"