from django.urls import path

from .controllers import crawl
from .views import CourseList

app_name = 'api'

urlpatterns = [
    path('courses/', CourseList.as_view(), name='course-list'),
    path('crawl/', crawl, name='crawl')
]


