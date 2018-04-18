from django.db import models

# Create your models here.
class Courses_timings(models.Model):
    course_num = models.CharField(max_length=8, primary_key=True)
    timings = models.CharField(max_length=50)
    def __str__(self):
        return self.course_num + ' having timings ' + self.timings

class Courses_info(models.Model):
    course_num = models.CharField(max_length=8, primary_key=True)
    course_name = models.CharField(max_length=50)
    course_instructor_name = models.CharField(max_length=50)
    course_credits = models.IntegerField()
    def __str__(self):
        s = "Course no. " + self.course_num + ", name: " + self.course_name + \
                ", instructor: " + self.course_instructor_name + ", credits: " \
                + self.course_credits
        return s
