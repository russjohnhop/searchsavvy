from django.urls import path

from . import views
from .views import CourseAPI, LessonAPI, CourseDetailsAPI, QuestionAPI, AnswerAPI, EnrollmentAPI, QuizAPI

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("courses", views.courses, name="courses"),
    path("courses/<int:course_id>", views.course, name="course"),
    path("enrol/<int:course_id>", views.enrol, name="enrol"),
    path("lesson/<int:course_id>", views.lesson, name="lesson"),
    path("quiz/<int:course_id>", views.quiz, name="quiz"),
    path("api/courses/", CourseAPI.as_view(), name="course-api"),
    path("api/lessons/", LessonAPI.as_view(), name="lesson-api"),
    path("api/courses/<str:quiz_title>/details", CourseDetailsAPI.as_view(), name="course-details-api"),
    path("api/questions/<int:question_id>", QuestionAPI.as_view(), name="question-api"),
    path("api/answers/<int:question_id>/", AnswerAPI.as_view(), name="answer-api"),
    path("api/enrollments/<int:course_id>", EnrollmentAPI.as_view(), name="enrollment-api"),
    path("api/quiz/<int:quiz_id>/", QuizAPI.as_view(), name="quiz-api"),
]