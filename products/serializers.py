from rest_framework import serializers
from .models import Product, Brand, Category


class CategorySerializer (serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name','image']
        



class BrandSerializer (serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    class Meta:
        model = Brand
        fields = ['name','image','category']


class ProductSerializer (serializers.ModelSerializer):

    # brand = serializers.StringRelatedField()
    # category = serializers.StringRelatedField()

    brand = BrandSerializer()
    category = CategorySerializer()

    price_with_discount = serializers.SerializerMethodField()





    def get_price_with_discount (self,product):
        return (product.price - product.price * .10)

    class Meta:
        model = Product
        fields = '__all__'
        

class CategoryDetailSerializer (serializers.ModelSerializer):

    products = ProductSerializer(source = 'product_category',many = True)

    class Meta:
        model = Category
        fields = ['name','image','products']


class BrandDetailSerializer (serializers.ModelSerializer):

    products = ProductSerializer(source = 'product_brand',many = True)
    category = serializers.StringRelatedField()

    class Meta:
        model = Brand
        fields = ['name','image','category','products']