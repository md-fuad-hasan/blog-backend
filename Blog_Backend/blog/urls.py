from django.urls import path 
from blog.views import (
    BlogListCreateAPIView,
    PersonalBlogListCreateAPIView,
)

urlpatterns = [
    path('',BlogListCreateAPIView.as_view(), name='blog'),
    path('user/',PersonalBlogListCreateAPIView.as_view(), name='personal'),
]