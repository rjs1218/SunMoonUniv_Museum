from django.db import models

# Create your models here.
class Introduction_guide(models.Model):
    title = models.CharField(max_length=200, null=False)
    image = models.ImageField(upload_to='introduction/', null=False)

class Introduction_history(models.Model):
    date = models.DateField(null=False)
    content = models.TextField(null=True)