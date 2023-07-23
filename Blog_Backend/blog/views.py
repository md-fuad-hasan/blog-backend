from rest_framework import generics
from blog.models import Blog
from blog.serializers import BlogSerializer


# Create your views here.

class BlogListCreateAPIView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

