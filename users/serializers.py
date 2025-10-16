
from rest_framework import serializers
from users.models import Author, admin_user, book, profile

class ProfileSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(source='user.phone_number')
    class Meta:
        model = profile
        fields = ["address","phone_number"]

# class book_serializer(serializers.ModelSerializer):
#     author = serializers.CharField(source='author.username')
#     title = serializers.CharField(max_length=255)
#     published_date = serializers.DateField()
#     class Meta:
#         model = book
#         fields = ["title", "author", "published_date"]




class AuthorSerializer(serializers.ModelSerializer):
    Number_of_books_written=serializers.SerializerMethodField()
    def get_Number_of_books_written(self,obj):
        Author_books= obj.book_set.all()
        counter=0
        for i in Author_books:
            counter+=1
        return counter

    class Meta:
        model = Author
        fields = (
            "Full_Name",
            "age",
            "phone_number",
            "Number_of_books_written",
        )


class BookSerializer(serializers.ModelSerializer):
    authors_list = serializers.CharField(source='authors', read_only=True)

    class Meta:
        model = book
        fields = (
            "name",
            "published",
            "authors",
            "authors_list",
        )