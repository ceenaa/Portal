from rest_framework.generics import ListAPIView, CreateAPIView

from .models import Course
from .serializers import CourseSerializer


# Create your views here.


class CourseList(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CreateCourse(CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
