from django.urls import path 
from blog.views import (
    BlogListAPIView,
    PersonalBlogListAPIView,
    PersonalBlogCreateAPIView,
    BlogDetailView,
)

urlpatterns = [
    path('',BlogListAPIView.as_view(), name='blog'),
    path('user/',PersonalBlogListAPIView.as_view(), name='personal_list'),
    path('create/',PersonalBlogCreateAPIView.as_view(), name='personal'),
    path('blog-detail/<slug>', BlogDetailView.as_view(), name='blog_detail'),
]