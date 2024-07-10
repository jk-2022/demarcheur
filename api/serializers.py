# store/serializers.py

from rest_framework import serializers
from product.models import Category, Product, ProductImages, Review
from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'email')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data.get('email', '')
        )
        return user

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields = ['id', 'image']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'user', 'review', 'rating']

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    image_files = serializers.ListField(
        child=serializers.ImageField(write_only=True), write_only=True, required=False)
    reviews = ReviewSerializer(many=True, read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'category', 'owner', 'images', 'image_files','reviews']
        
    def create(self, validated_data):
        print(validated_data)
        image_files = validated_data.pop("image_files",[])
        product = Product.objects.create(**validated_data)
        for image in image_files:
            ProductImages.objects.create(product=product, image=image)
        return product
    
    def update(self, instance, validated_data):
        image_files = validated_data.pop('image_files', [])
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.category = validated_data.get('category', instance.category)
        instance.save()

        # Remove existing images if new ones are provided
        if image_files:
            instance.images.all().delete()
            for image_file in image_files:
                ProductImages.objects.create(product=instance, image=image_file)
        
        return instance
