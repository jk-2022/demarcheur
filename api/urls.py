# store/urls.py

from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('categories/', CategoryList.as_view(), name='category-list'),
    path('categories/create/', CategoryCreateAPIView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailAPIView.as_view(), name='category-detail'),
    path('types/', TypeListCreateAPIView.as_view(), name='type-list-create'),
    path('types/<int:pk>/', TypeDetailAPIView.as_view(), name='type-detail'),
    path('villes/', VilleListCreateAPIView.as_view(), name='ville-list-create'),
    path('villes/<int:pk>/', VilleDetailAPIView.as_view(), name='ville-detail'),
    path('products/', ProductList.as_view(), name='product-list'),
    path('products/create/', ProductCreateView.as_view(), name='product-create'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('reviews/', ReviewListCreate.as_view(), name='review-list-create'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
    path('add_user_to_group/', add_user_to_group, name='add_user_to_group'),
]
