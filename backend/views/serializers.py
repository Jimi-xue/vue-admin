from backend.models import Book
from rest_framework import serializers
from django.contrib.auth.models import User

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id','book_name','add_time' )

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','is_superuser')