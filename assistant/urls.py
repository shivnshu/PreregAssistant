from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^courses_list', views.courses_list, name='courses_list'),
        url(r'^course_detail', views.get_course_detail, name='get_course_detail'),
        url(r'^get_non_conflicting_courses', views.get_non_conflicting_courses, name='get_non_conflicting_courses'),
        url(r'^course_add', views.course_add, name='course_add')
]
