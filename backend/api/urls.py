from django.urls import path

from .controllers import crawl
from .views import CourseList, createChosenCourse, ChosenCourseList

app_name = 'api'

urlpatterns = [
    path('courses/', CourseList.as_view(), name='course-list'),
    path('crawl/', crawl, name='crawl'),
    path('choose-courses/', createChosenCourse, name='chosen-course-list'),
    path('chosen-courses/', ChosenCourseList.as_view(), name='chosen-course-list'),
]
