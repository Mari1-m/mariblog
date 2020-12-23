from django.db import models

# Create your models here.
class memories(models.Model):
    memories_image = models.ImageField(upload_to="memories_images/")
    memories_text = models.CharField(max_length=300)
