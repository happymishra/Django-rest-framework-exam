from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from rest_framework import status
from .serializers import ProductSerializer
from .permissions import IsAdminOrReadOnly


class ProductList(APIView):
    permission_classes = (IsAdminOrReadOnly,)

    def get(self, request):
        products = Product.objects.all()
        serializers = ProductSerializer(products, many=True)

        return Response(serializers.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


