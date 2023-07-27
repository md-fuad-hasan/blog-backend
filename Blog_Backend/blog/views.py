from rest_framework import generics,parsers
from blog.models import Blog
from blog.serializers import (
    BlogSerializer,
    BlogCreateSerializer
)
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class BlogListAPIView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class PersonalBlogCreateAPIView(generics.CreateAPIView):

    serializer_class = BlogCreateSerializer
    queryset = Blog.objects.all()

    permission_classes = [IsAuthenticated]
    parser_classes = [parsers.FormParser,parsers.MultiPartParser]



class PersonalBlogListAPIView(generics.ListAPIView):

    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Blog.objects.all()
        id = self.request.query_params.get('user',None)
        if id is not None:
            queryset = Blog.objects.filter(author=id)

        return queryset

class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BlogCreateSerializer
    queryset = Blog.objects.all()
    permission_classes = [IsAuthenticated]
    lookup_field = 'slug'
