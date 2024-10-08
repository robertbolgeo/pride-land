from django.db import models
from medias.models import Media

# Create your models here.
class Hero(models.Model):
    img_url = models.ForeignKey(Media, on_delete= models.SET_NULL, null=True)
    site_desc = models.TextField(null=False)

    logo = models.ImageField(default="default.jpg", upload_to="image_url")

    def __str__(self):
        return f"img url: {self.img_url}"

