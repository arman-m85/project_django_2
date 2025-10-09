
from rest_framework import serializers
from users.models import book, profile

class ProfileSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(source='user.phone_number')
    class Meta:
        model = profile
        fields = ["address","phone_number"]

class book_serializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username')
    title = serializers.CharField(max_length=255)
    published_date = serializers.DateField()
    class Meta:
        model = book
        fields = ["title", "author", "published_date"]