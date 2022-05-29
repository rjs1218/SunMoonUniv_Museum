from django.db import models

# Create your models here.
class Exhibition_work(models.Model):
    title = models.CharField(max_length=200, null=False)
    image = models.ImageField(upload_to='exhibition_work/', null=False)
    content = models.TextField(null=True)