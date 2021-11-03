from rest_framework import serializers
from .models import *

class BookSerializer1(serializers.ModelSerializer):
    author=serializers.StringRelatedField()
    class Meta:
        model=Book
        fields=['title', 'id', 'author']

class AuthorSerializer1(serializers.ModelSerializer):
    #book_set=serializers.StringRelatedField(many=True)
    book_set = serializers.SlugRelatedField(slug_field='title', many=True, read_only=True)
    class Meta:
        model=Author
        fields=['last', 'first', 'year', 'img', 'book_set']
