from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^courses_list', views.courses_list, name='courses_list'),
        url(r'^course_detail', views.get_course_detail, name='get_course_detail')
]
