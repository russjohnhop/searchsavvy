from django.contrib.auth.models import AbstractUser
from django.db import models
from embed_video.fields import EmbedVideoField


class User(AbstractUser):
    bio = models.TextField(blank=True)
    avatar = models.URLField()

    def __str__(self):
        return self.username

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    skills = models.TextField()
    modules = models.TextField()

    def __str__(self):
        return self.title


class Lesson(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    video_link = EmbedVideoField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Quiz(models.Model):
    title = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'course_id': self.course.id,
        }


class Question(models.Model):
    text = models.TextField()
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    def serialize(self):
        return {
            'id': self.id,
            'text': self.text,
            'quiz': self.quiz.id, 
        }


class Answer(models.Model):
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    current_lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, null=True, blank=True)
    completed_lessons = models.ManyToManyField(Lesson, related_name='completed_by', blank=True)
    completed_quizzes = models.ManyToManyField(Quiz, related_name='completed_by', blank=True)

    def __str__(self):
        return f'{self.user.username} - {self.course.title}'

    

