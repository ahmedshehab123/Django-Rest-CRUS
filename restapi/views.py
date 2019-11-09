from rest_framework import viewsets
from .models import Products, News
from .Serializers import ProductSerializer,NewsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class productlist(viewsets.ModelViewSet):
    queryset = Products.objects.all().order_by('id')
    serializer_class = ProductSerializer


class newslist(viewsets.ModelViewSet):
    queryset = News.objects.all().order_by('id')
    serializer_class = NewsSerializer

# def get(self,request):
#     product=Products.objects.all()
#     serilaizer = ProductSerializer(product, many=True)
#     return Response(serilaizer.data)
# def post(request):
#     pass

# class ProductsViewSet(viewsets.ModelViewSet):
#     queryset = Products.objects.all()
#     serializer_class = ProductSerializer
