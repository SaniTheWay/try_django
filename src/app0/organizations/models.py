from django.db import models

# Create your models here.


class Organizations(models.Model):
    org_name = models.CharField(max_length=255)
    location = models.CharField(max_length=150)
    # contest_org
    # projects
