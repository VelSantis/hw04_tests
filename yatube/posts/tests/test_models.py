from django.contrib.auth import get_user_model
from django.test import TestCase

from ..models import Group, Post

User = get_user_model()


class PostModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='Tanos')
        cls.post = Post.objects.create(
            text='Текст в котором много много символов для теста.',
            author=cls.user,
        )

    def test_post_str(self):
        """Проверка __str__ у post."""
        self.assertEqual(str(self.post), self.post.text[:15])


class GroupModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='Tanos')
        cls.group = Group.objects.create(
            title='Тестовая группа',
            slug='Тестовый слаг',
            description='Тестовое описание',
        )

    def test_group_str(self):
        """Проверка __str__ у group."""
        self.assertEqual(str(self.group), self.group.title)
