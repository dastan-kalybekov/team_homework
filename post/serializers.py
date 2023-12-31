from django.db import IntegrityError
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Post, Rating, Comment


class PostSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ['user']

    def get_rating(self, obj):
        ratings = []
        rating_queryset = Rating.objects.values('rating').filter(post=obj.id)
        if rating_queryset.exists():
            for rating in rating_queryset:
                ratings.append(rating["rating"])
            return sum(ratings) / len(ratings)
        return 0


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ['author']


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = "__all__"
        read_only_fields = ['user']

    def create(self, validated_data):
        rating = Rating(**validated_data)
        try:
            rating.save()
        except IntegrityError:
            raise ValidationError('Невозможно сохранить. Вы пытаетесь поставить рейтинг, к этому посту еще раз !')
        else:
            return rating
