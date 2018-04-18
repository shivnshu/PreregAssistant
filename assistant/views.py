from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Courses_timings, Courses_info
import json

def index(request):
    courses_timings_list = Courses_timings.objects.all()
    context = {'dropdown_courses': courses_timings_list}
    return render(request, 'assistant/index.html', context)
    # return HttpResponse("Welcome to assistant!")

def courses_list(request):
    courses_timings_list = Courses_timings.objects.all()
    # courses_info_list = Courses_info.objects.filter(course_num=)
    context = {'courses_details': courses_timings_list}
    return render(request, 'assistant/courses_list.html', context)

def get_course_detail(request):
    course_num = request.GET.get('num', '')
    try:
        course_details = Courses_timings.objects.get(course_num=course_num)
        data = {
                'course_num': course_details.course_num,
                'timings': course_details.timings,
                'course_name': '',
                'instructor': '',
                'credits': ''
                }
        return HttpResponse(json.dumps(data), content_type="application/json")
    except:
        return HttpResponse("")
