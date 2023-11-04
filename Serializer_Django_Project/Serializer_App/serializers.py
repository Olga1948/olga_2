from rest_framework import serializers
from .models import Product, Rating, Comment


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class ProductRatingCommentsSerializer(serializers.Serializer):
    product_id = serializers.IntegerField() #поле для ввода id товара
    rating = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()

    def get_rating(self, obj):
        my_product = Product.objects.get(id=obj['product_id'])
        ratings = Rating.objects.filter(product=my_product)
        total_ratings = ratings.count()
        if total_ratings == 0:
            average_rating = 0
        else:
            average_rating = sum(rating_object.rating for rating_object in ratings)/total_ratings
        return average_rating

    def get_comments(self, obj):
        my_product = Product.objects.get(id=obj['product_id'])
        comments = Comment.objects.filter(product=my_product)
        comment_data = CommentSerializer(comments, many=True).data
        return comment_data
