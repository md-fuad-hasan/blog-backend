from rest_framework import serializers
from .models import Account,AccountDetail


from django.contrib.auth.hashers import check_password

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id','email','username','password']
        extra_kwargs = {'password':{'style':{'input_type':'password'},'write_only':True}}

    def create(self,validated_data):
        user = Account.objects.create_user(
            email=validated_data['email'],
            username= validated_data['username'],
            password=validated_data['password']
        )

        return user


class AccountDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountDetail
        fields = '__all__'


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True,style={'input_type': 'password'},)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:

            
            user = Account.objects.filter(username=username).first()
            
            if user is None:
                user = Account.objects.filter(email=username).first()
                
                if user is None:
                    msg = 'Username or Email not Found'
                    raise serializers.ValidationError(msg, code='authorization')
                
            
            if check_password(password,user.password):
                attrs['user'] = user
                return attrs
            else:
                msg = 'Password is incorrect'
                raise serializers.ValidationError(msg, code='authorization')

           
        else:
            msg = 'Must include "username" and "password".'
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs