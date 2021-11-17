from contextlib import nullcontext
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import BooleanField
from django.conf import settings
from django.conf import settings

# Create your models here.

User = settings.AUTH_USER_MODEL


class Showcase(models.Model):
    YES = "ys"
    NO = "no"
    IDEA = "ID"
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
#     user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    title = models.CharField(
        max_length=120)  # maxlength *required
    description = models.TextField(blank=True, null=True)
    active = models.CharField(
        max_length=2,
        choices=[
            (YES, 'Yes'),
            (NO, 'No'),
            (IDEA, 'Just An Idea'),
        ],
        # default=NO
    )
    featured = models.BooleanField(blank=True, null=True)
    project_img = models.ImageField(upload_to='img/')
    project_link = models.URLField(help_text="example@example.com")
