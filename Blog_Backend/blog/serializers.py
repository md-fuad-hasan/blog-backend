from rest_framework import serializers
from blog.models import Blog 


class BlogSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField()

    class Meta:
        model = Blog 
        fields = '__all__'

    def get_author_name(self, obj):
         return obj.author.username


        
