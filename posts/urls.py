from django.urls import path

from .views import PostList, PostDetail
from allauth.socialaccount.models import SocialAccount, SocialApp, SocialToken

urlpatterns = [
    path("<int:pk>/", PostDetail.as_view(), name="post_detail"),
    path("", PostList.as_view(), name="post_list"),
]