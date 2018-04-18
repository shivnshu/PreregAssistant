from django.contrib import admin

# Register your models here.
from .models import Courses_timings, Courses_info

admin.site.register(Courses_timings)
admin.site.register(Courses_info)
