from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Courses_timings, Courses_info

def index(request):
    context = {}
    return render(request, 'assistant/index.html', context)
    # return HttpResponse("Welcome to assistant!")

def courses_list(request):
    courses_timings_list = Courses_timings.objects.all()
    context = {'courses_timings_list': courses_timings_list}
    return render(request, 'assistant/courses_list.html', context)
