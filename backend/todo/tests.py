from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Todo

class TodoModelTest(TestCase):
    def test_todo_creation(self):
        todo = Todo.objects.create(
            title="Test Todo",
            description="Test Description",
            completed=False
        )
        self.assertEqual(todo.title, "Test Todo")
        self.assertFalse(todo.completed)

class TodoAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.client.force_authenticate(user=self.user)

    def test_create_todo(self):
        data = {
            'title': 'Test Todo',
            'description': 'Test Description',
            'completed': False
        }
        response = self.client.post('/api/todos/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Todo.objects.count(), 1)

    def test_get_todos(self):
        Todo.objects.create(title="Test Todo", description="Test")
        response = self.client.get('/api/todos/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)