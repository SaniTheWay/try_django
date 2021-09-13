from django.db import models
from django.db.models.fields import BooleanField

# Create your models here.

class Showcase(models.Model):
    YES="ys"
    NO="no"
    IDEA="ID"

    title = models.CharField(max_length=120) #maxlength *required
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=1000)
    active = models.CharField(max_length=2, 
                                choices=[
                                        (YES, 'Yes'),
                                        (NO, 'No'),
                                        (IDEA, 'Just An Idea'),
                                        ], 
                                default=NO)
    summary = models.TextField(blank=True, null=True)
    featured = models.BooleanField()