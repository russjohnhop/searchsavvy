from django.contrib import admin
from django import forms
from django.db import models
from .models import User, Quiz, Lesson, Course, Question, Answer, Enrollment

# Register your models here.

admin.site.register(User)
admin.site.register(Quiz)
admin.site.register(Lesson)
admin.site.register(Course)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Enrollment)


