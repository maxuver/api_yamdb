from rest_framework import serializers, validators
from rest_framework.relations import SlugRelatedField

from reviews.models import Review, Title


class ReviewSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = ('id', 'text', 'author', 'score', 'pub_date')
        model = Review


class ReviewListSerializer(serializers.ModelSerializer):
    results = ReviewSerializer(many=True)

    class Meta:
        model = Review
        fields = ('count', 'next', 'previous', 'results')
