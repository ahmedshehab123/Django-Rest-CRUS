from rest_framework import serializers
from .models import Products,News
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        # fields = ('name','price')
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        # fields = ('name','price')
        fields = '__all__'