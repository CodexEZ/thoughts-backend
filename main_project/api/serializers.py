from rest_framework import serializers
from api.models import Users, Posts

class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = '__all__'

class PostsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ['user','title','desc']
class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password =  serializers.CharField()
    