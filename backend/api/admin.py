from django.contrib import admin

# Register your models here.

from .models import Course, Time

admin.site.register(Course)
admin.site.register(Time)