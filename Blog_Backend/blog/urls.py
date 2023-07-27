from django.urls import path 
from blog.views import (
    BlogListAPIView,
    PersonalBlogListAPIView,
    PersonalBlogCreateAPIView,
)

urlpatterns = [
    path('',BlogListAPIView.as_view(), name='blog'),
    path('user/',PersonalBlogListAPIView.as_view(), name='personal_list'),
    path('create/',PersonalBlogCreateAPIView.as_view(), name='personal'),
]