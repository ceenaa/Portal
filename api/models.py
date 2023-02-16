from django.db import models


# Create your models here.

class Time(models.Model):
    day = models.CharField(max_length=100)
    start_time = models.CharField(max_length=100)
    end_time = models.CharField(max_length=100)

    def __str__(self):
        return self.day + " " + self.start_time + " " + self.end_time


class Course(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    group = models.CharField(max_length=100)
    class_times = models.ManyToManyField(Time, related_name='Course')
    exam_time = models.ForeignKey(Time, on_delete=models.CASCADE, related_name='exam')

    def __str__(self):
        return self.name
