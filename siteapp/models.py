from django.db import models

# Create your models here.
class Introduction_history(models.Model):
    date = models.DateField(null=False)
    content = models.TextField(null=True)