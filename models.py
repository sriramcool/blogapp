from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class tech_blog(models.Model):

    name = models.CharField(max_length = 30)
    cover_image = models.ImageField(upload_to = 'tech/coverimage')
    image2 = models.ImageField(upload_to = 'tech/image2', blank= True)
    image3 = models.ImageField(upload_to = 'tech/image3', blank = True )
    q1 = models.TextField(blank=True)
    desc1 = models.TextField(blank=True)
    q2 = models.TextField(blank=True)
    desc2 = models.TextField(blank=True)
    q3 = models.TextField(blank=True)
    desc3 = models.TextField(blank=True)
    special_artice = models.BooleanField(default = False)
    more = models.BooleanField(default=False)

#car = Car.objects.get(name="chevy") - use to get the object
#car.image1.path -- returns file location