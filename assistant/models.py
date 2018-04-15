from django.db import models

# Create your models here.
class Courses_timings(models.Model):
    course_num = models.CharField(max_length=8, primary_key=True)
    timings = models.TimeField('Timings of the course')

class Courses_info(models.Model):
    course_num = models.ForeignKey(Courses_timings, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=50)
    course_instructor_name = models.CharField(max_length=50)
    course_credits = models.IntegerField()
