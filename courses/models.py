from datetime import date

from django.db import models


class Course(models.Model):
    course_name = models.CharField(max_length=100)
    price = models.FloatField()
    detail_info = models.TextField()
    start_time = models.DateField(default=date.today)
    end_time = models.DateField()
    image = models.ImageField(upload_to='Images/')
