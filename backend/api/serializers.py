from rest_framework import serializers
from .models import Course, Time, ChosenCourse


class ClassTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Time
        fields = '__all__'


class ForeignClassTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Time
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class_times = ClassTimeSerializer(many=True, read_only=True)
    exam_time = ForeignClassTimeSerializer(read_only=True)

    class Meta:
        model = Course
        fields = '__all__'


class ChosenCourseSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)

    class Meta:
        model = ChosenCourse
        fields = '__all__'
