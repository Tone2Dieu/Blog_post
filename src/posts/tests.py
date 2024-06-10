from django.test import TestCase
from .models import Post
from django.contrib.auth import get_user_model
# Create your tests here.


class PostTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create(
            username='testuser',
            email='testuser@gmail.com',
            password='@Trone2Rah'
        )

        cls.post = Post.objects.create(
            title='python',
            body='the best language',
            author=cls.user
        )

    def test_model_post(self):
        self.assertEqual(self.post.author.username, 'testuser')
        self.assertEqual(self.post.title, 'python')
        self.assertEqual(self.post.body, 'the best language')
        self.assertEqual(str(self.post), 'python')
