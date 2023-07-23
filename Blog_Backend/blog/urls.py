from django.urls import path 
from blog.views import BlogListCreateAPIView

urlpatterns = [
    path('',BlogListCreateAPIView.as_view(), name='blog')
]