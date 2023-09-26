from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from ..models import Course, Enrollment

class ViewsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.course = Course.objects.create(title='Test Course', skills='Skill 1\nSkill 2')

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_login_view(self):
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'testpass'})
        self.assertEqual(response.status_code, 302)  # Successful login should redirect
        self.assertRedirects(response, reverse('index'))

    def test_logout_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)  # Successful logout should redirect
        self.assertRedirects(response, reverse('index'))

    
    def test_enrollment_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('enrol', args=[self.course.id]))
        self.assertEqual(response.status_code, 200)

    def test_course_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('course', args=[self.course.id]))
        self.assertEqual(response.status_code, 200)

    def test_lesson_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('lesson', args=[self.course.id]))
        self.assertEqual(response.status_code, 200)

    def test_quiz_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('quiz', args=[self.course.id]))
        self.assertEqual(response.status_code, 200)