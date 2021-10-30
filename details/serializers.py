from rest_framework import serializers
from .models import Author,Book
class AuthorSerializer(serializers.ModelSerializer):
    books=serializers.PrimaryKeyRelatedField(read_only=True,many=True)
    class Meta:
        model=Author
        fields=["first_name","last_name","birthday","books"]
class BookSerializer(serializers.ModelSerializer):
    author=serializers.PrimaryKeyRelatedField(read_only=True,many=False)
    class Meta:
        model=Book
        fields=["id","name","genere","author","date_writed"]
