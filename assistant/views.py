from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Courses_timings, Courses_info
import json

def check_time_conflict(times, busy_times):
    times = times.replace(':', '')
    busy_times = busy_times.replace(':', '')
    
    times = times.split('-')
    busy_times = busy_times.split('-')

    smaller = min(int(times[0]), int(busy_times[0]))
    larger = max(int(times[1]), int(busy_times[1]))

    if (larger-smaller < int(times[1])-int(times[0])+int(busy_times[1])-int(busy_times[0])):
        return True
    return False

def check_days_conflict(days, busy_days):
    days = list(days)
    busy_days = list(busy_days)
    for i in range(len(days)):
        if days[i].islower():
            days[i-1] += days[i]
            days.pop(i)
            break
    for i in range(len(busy_days)):
        if busy_days[i].islower():
            busy_days[i-1] += busy_days[i]
            busy_days.pop(i)
            break

    for c1 in days:
        for c2 in busy_days:
            if (c1 == c2):
                return True

    return False

def check_course_conflict(timing, busy_timings):
    timing = timing.split()
    for busy_timing in busy_timings:
        busy_timing = busy_timing.split()
        for i in range(len(timing)//2):
            days = timing[2*i]
            for j in range(len(busy_timing)//2):
                busy_days = busy_timing[2*j]
                if (not check_days_conflict(days, busy_days)):
                    continue
                times = timing[2*i+1]
                busy_times = busy_timing[2*j+1]
                if (check_time_conflict(times, busy_times)):
                    return True
    return False

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
    # print(courses_list)
    courses_list_timings = []
    for course_num in courses_list:
        course = Courses_timings.objects.get(course_num=course_num)
        courses_list_timings.append(course.timings)
    # print(courses_list_timings)
    all_courses = Courses_timings.objects.all()
    ans_courses = []
    for course in all_courses:
        # print(len(course.timings.split()))
        if (not check_course_conflict(course.timings, courses_list_timings)):
            ans_courses.append(course.course_num)
    print(ans_courses)
    return HttpResponse("")

def course_add(request):
    course_num = request.GET.get('course_num', '')
    course_name = request.GET.get('course_name', '')
    course_instructor_name = request.GET.get('course_instructor', '')
    course_credits = request.GET.get('course_credits', '')
    course_timings = request.GET.get('course_timings', '')
    # print(course_num, course_name, course_instructor_name, course_credits, course_timings)
    p = Courses_timings(course_num=course_num, timings=course_timings)
    p.save()
    q = Courses_info(course_num=course_num, course_name=course_name, course_instructor_name=course_instructor_name, course_credits=int(course_credits))
    q.save()
    return HttpResponse("")
