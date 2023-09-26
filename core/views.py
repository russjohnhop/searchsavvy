from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.db import IntegrityError
from .models import User, Quiz, Lesson, Course, Question, Answer, Enrollment
from django.views import View
from django.core import serializers
import json
from itertools import zip_longest


def index(request):

    return render(request, "core/index.html")

def login_view(request):
    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "core/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "core/login.html")
    
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "core/register.html", {
                "message": "Passwords must match."
            })

        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "core/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "core/register.html")
    

def courses(request):
    course_list = Course.objects.all()
    return render(request, "core/courses.html", {
        "courses" : course_list
    })


def course(request, course_id):
    user_course = Course.objects.get(pk=course_id)
    user = request.user

    complete_status = False
    enrollment = None

    if user.is_authenticated:
        try:
            enrollment = Enrollment.objects.get(user=user, course=user_course)
            complete_status = enrollment.completed
        except ObjectDoesNotExist:
            complete_status = False

    content_lines = user_course.skills.split("\n")
    content_lines = [line.strip() for line in content_lines if line.strip()]

    modules = user_course.modules.split("\n")
    modules = [line.strip() for line in modules if line.strip()]

    return render(request, "core/course.html", {
        "course" : user_course,
        "user" : user,
        "completed" : complete_status,
        "content_lines" : content_lines,
        "modules" : modules,
        "enrollment" : enrollment,
    })


def enrol(request, course_id):
    user_course = Course.objects.get(pk=course_id)
    user = request.user

    try:
        enrollment = Enrollment.objects.get(user=user, course=user_course)
        complete_status = enrollment.completed
    except ObjectDoesNotExist:
        enrollment = None
        complete_status = False

    if request.method == "POST":
        complete_status = not complete_status

        if enrollment:
            enrollment.completed = complete_status
            enrollment.save()
        else:
            enrollment = Enrollment.objects.create(user=user, course=user_course, completed=complete_status)

    return render(request, "core/enrol.html", {
        "course": user_course,
        "user": user,
        "completed": complete_status
    })



def lesson(request, course_id):
    user_course = Course.objects.get(pk=course_id)
    user = request.user

    enrollment = get_object_or_404(Enrollment, user=user, course=course_id)
    complete_status = enrollment.completed

    user_lessons = Lesson.objects.filter(course=course_id)
    lesson_contents_list = []  # To store content for each lesson

    for lesson in user_lessons:
        lesson_contents = lesson.content.split("\n")
        lesson_contents = [line.strip() for line in lesson_contents if line.strip()]
        lesson_contents_list.append(lesson_contents)

    # Zip the lessons and their contents together
    lessons_and_contents = zip_longest(user_lessons, lesson_contents_list)


    return render(request, "core/lesson.html", {
    "lessons" : user_lessons,
    "course" : user_course,
    "user" : user,
    "completed" : complete_status,
    "lessons_and_contents" : lessons_and_contents
})


def quiz(request, course_id):

    if request.method == "GET":

        user_course = Course.objects.get(pk=course_id)
        user = request.user


        user_quiz = Quiz.objects.get(course=course_id)


        question = Question.objects.filter(quiz=user_quiz).first()
        print("question: " ,  question)


        answers = Answer.objects.filter(question=question)

        correct_answer = Answer.objects.get(question=question, is_correct=True)

        return render(request, "core/quiz.html", {
        "course" : user_course,
        "user" : user,
        "quiz" : user_quiz,
        "question" : question,
        "answers" : answers,
        "correct_answer" : correct_answer,
    })


# Serialization views

class CourseAPI(View):
    def get(self, request):
        queryset = Course.objects.all()
        serialized_data = [obj.serialize() for obj in queryset]
        return JsonResponse(serialized_data, safe=False)
    

class LessonAPI(View):
    def get(self, request):
        queryset = Lesson.objects.all()
        serialized_data = [obj.serialize() for obj in queryset]
        return JsonResponse(serialized_data, safe=False)

class CourseDetailsAPI(View):
    def get(self, request, quiz_title):
        try:
            course = Course.objects.get(title=quiz_title)
            serialized_data = quiz.course.serialize()
            return JsonResponse(serialized_data)
        except Course.DoesNotExist:
            return JsonResponse({"error": "Course not found."}, status=404)
        
class QuizAPI(View):
    def get(self, request, quiz_id):
        try:
            quiz = Quiz.objects.get(pk=quiz_id)
            serialized_data = quiz.serialize()
            return JsonResponse(serialized_data)
        except Quiz.DoesNotExist:
            return JsonResponse({'error': 'Quiz not found'}, status=404)

class QuestionAPI(View):
    def get(self, request,question_id):
        queryset = Question.objects.all()
        serialized_data = [obj.serialize() for obj in queryset]
        return JsonResponse(serialized_data, safe=False)

class AnswerAPI(View):
    def get(self, request, question_id):
        answers = Answer.objects.filter(question_id=question_id)
        # Serialize the queryset to a list of dictionaries
        serialized_data = list(answers.values())
        return JsonResponse(serialized_data, safe=False)

class EnrollmentAPI(View):
    def get(self, request, course_id):
        try:
            queryset = Enrollment.objects.filter(course_id=course_id)
            serialized_data = [obj.serialize() for obj in queryset]
            return JsonResponse(serialized_data, safe=False)

        except Enrollment.DoesNotExist:
            return JsonResponse({"error": "Enrollment not found."}, status=404)

    def put(self, request, course_id):
        enrollment = get_object_or_404(Enrollment, course_id=course_id)
        
        try:
            request_data = json.loads(request.body.decode('utf-8'))
            completed_status = request_data.get("completed")
            
            if completed_status is not None:
                enrollment.completed = completed_status
                enrollment.save()
                return JsonResponse({"message": "Enrollment updated successfully"})
            else:
                return JsonResponse({"error": "Missing 'completed' field in request data"}, status=400)
        
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data in request"}, status=400)
        
    
        
    

