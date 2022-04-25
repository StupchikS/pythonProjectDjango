from django.db import models


class ElectricCarDir(models.Model):
    car_name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='electric_car_dir/images/')
    url = models.URLField(blank=True)

