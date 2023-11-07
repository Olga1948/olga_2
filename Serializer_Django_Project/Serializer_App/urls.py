from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ProductList, category_list, ArticleDetail

urlpatterns = [
    path('products/', ProductList.as_view(), name='product-list'),
    path('categories/', category_list, name='category-list'),
    path('articles/<int:pk>/', ArticleDetail.as_view(), name='article-detail')
]

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns += router.urls
