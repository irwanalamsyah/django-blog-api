from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Post


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.user = get_user_model().objects.create_user(
            username="testuser",
            email="test@email.com",
            password="secret",
        )
        
        cls.post = Post.objects.create(
            author=cls.user,
            title="This is Title",
            body="Nice body content",
        )
        
    def test_post_model(self):
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(self.post.title, "This is Title")
        self.assertEqual(self.post.body, "Nice body content")
        self.assertEqual(str(self.post), "This is Title")
    
