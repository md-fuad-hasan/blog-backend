from rest_framework import generics
from blog.models import Blog
from blog.serializers import BlogSerializer


# Create your views here.

class BlogListCreateAPIView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class PersonalBlogListCreateAPIView(generics.ListCreateAPIView):

    serializer_class = BlogSerializer

    def get_queryset(self):
        queryset = Blog.objects.all()
        id = self.request.query_params.get('user',None)
        if id is not None:
            queryset = Blog.objects.filter(author=id)

        return queryset
