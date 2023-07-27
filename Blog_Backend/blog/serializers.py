from rest_framework import serializers
from blog.models import Blog 


class BlogSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField()
    blog_content = serializers.SerializerMethodField()

    class Meta:
        model = Blog 
        exclude = ['id']

    def get_author_name(self, obj):
         return obj.author.username

    def get_blog_content(self, blog):
        return str(blog.blog_content)[0:500]



class BlogCreateSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Blog 
        fields = '__all__'

    def get_author_name(self, obj):
         return obj.author.username


        
