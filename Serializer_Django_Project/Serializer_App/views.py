from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer, ProductSerializer, CategorySerializer, ArticleSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product, Category, Article
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveUpdateDestroyAPIView


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProductList(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def category_list(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


class ArticleDetail(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
