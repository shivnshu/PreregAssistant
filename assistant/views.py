from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Courses_timings, Courses_info
import json

def check_course_conflict(timing, timings):
    return True

def index(request):
    courses_timings_list = Courses_timings.objects.all()
    context = {'dropdown_courses': courses_timings_list}
    return render(request, 'assistant/index.html', context)
    # return HttpResponse("Welcome to assistant!")

def courses_list(request):
    courses_timings_list = Courses_timings.objects.all()
    details = []
    for course_timings in courses_timings_list:
        course_info = Courses_info.objects.get(course_num=course_timings.course_num)
        s = {
                "course_num": course_timings.course_num,
                "course_name": course_info.course_name,
                "course_instructor_name": course_info.course_instructor_name,
                "course_credits": course_info.course_credits,
                "course_timings": course_timings.timings
                }
        details.append(s)
    context = {'courses_details': details}
    return render(request, 'assistant/courses_list.html', context)

def get_course_detail(request):
    course_num = request.GET.get('num', '')
    courses_list = request.GET.get('courses_list', '')
    # print(courses_list)
    try:
        course_details = Courses_timings.objects.get(course_num=course_num)
        course_info = Courses_info.objects.get(course_num=course_num)
        data = {
                'course_num': course_details.course_num,
                'timings': course_details.timings,
                'course_name': course_info.course_name,
                'instructor': course_info.course_instructor_name,
                'credits': course_info.course_credits
                }
        return HttpResponse(json.dumps(data), content_type="application/json")
    except:
        return HttpResponse("")

def get_non_conflicting_courses(request):
    courses_list = request.GET.get('courses_list', '')
    courses_list = courses_list.split()
    print(courses_list)
    courses_list_timings = []
    for course_num in courses_list:
        course = Courses_timings.objects.get(course_num=course_num)
        courses_list_timings.append(course.timings)
    print(courses_list_timings)
    all_courses = Courses_timings.objects.all()
    ans_courses = []
    for course in all_courses:
        if (not check_course_conflict(course.timings, courses_list_timings)):
            ans_courses.append(course.course_num)
    print(ans_courses)
    return HttpResponse("")

def course_add(request):
    return HttpResponse("")
