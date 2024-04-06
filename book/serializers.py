from .models import Book, Author, Publisher
from rest_framework import serializers


class AuthorSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
        extra_kwargs = {
            'name': {'required': True},
            'bio': {'required': True},
        }
        read_only_fields = ('id', 'name')


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'
        extra_kwargs = {
            'name': {'required': True},
            'email': {'required': True},
            'phone_number': {'required': True},
            'address': {'required': True},
        }
        read_only_fields = ('id', 'name')


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'publisher', 'genre', 'price', 'publication_date', 'updated_at']
        extra_kwargs = {
            'title': {'required': True},
            'author': {'required': True},
            'genre': {'required': True},
            'publisher': {'required': True},
            'price': {'required': True},
            'publication_date': {'required': True},
        }
        read_only_fields = ('id', 'title')

    def validate(self, data):
        if (
                (
                        self.instance is None or
                        self.instance.title is None
                ) and
                data.get("title", None) is None
        ):
            raise serializers.ValidationError(
                {"IntegrityError": "Title must be provided in order to create a book"}
            )
        if (
                (
                        self.instance is None or
                        self.instance.genre is None
                ) and
                data.get("genre", None) is None
        ):
            raise serializers.ValidationError(
                {"IntegrityError": "Genre must be provided in order to create a book"}
            )
        return data

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['author'] = {
            "id": instance.author.id,
            "name": instance.author.name,
            "bio": instance.author.bio,
        }
        rep['publisher'] = {
            "id": instance.publisher.id,
            "name": instance.publisher.name,
            "email": instance.publisher.email,
            "phone_number": instance.publisher.phone_number,
            "address": instance.publisher.address,
        }
        return rep
