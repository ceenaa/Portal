from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, ListCreateAPIView

from .controllers import checkCoherence
from .models import Course, ChosenCourse
from .serializers import CourseSerializer, ChosenCourseSerializer


# Create your views here.


class CourseList(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


@api_view(['POST'])
def createChosenCourse(request):
    if request.method == 'POST':
        course_ids = request.data['course_ids']
        for course_id in course_ids:
            course = Course.objects.get(id=course_id)
            if not checkCoherence(course):
                return JsonResponse({'error': 'Course has coherent'}, status=400)
            chosen_course = ChosenCourse.objects.create(course=course)
            chosen_course.save()
        return JsonResponse({'success': 'Course added successfully'}, status=200)


class CreateCourse(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class ChosenCourseList(ListAPIView):
    queryset = ChosenCourse.objects.all()
    serializer_class = ChosenCourseSerializer
