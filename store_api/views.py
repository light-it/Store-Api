from store_api.models import Category, Item
from store_api.serializers import CategorySerializer, ItemSerializer
from django.shortcuts import render
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response


class IndexView(View):

    def get(self, request):
        return render(request, 'index.html')


class CategoryListView(APIView):

    def get(self, request):
        response = Category.objects.all()
        serializer = CategorySerializer(response, many=True)
        return Response(serializer.data)


class ItemListView(APIView):

    def get(self, request):
        response = Item.objects.all()
        serializer = ItemSerializer(response, many=True)
        return Response(serializer.data)


class ItemDetailView(APIView):

    def get(self, request, pk):
        if Item.objects.filter(pk=pk).exists():
            response = Item.objects.get(pk=pk)
            serializer = ItemSerializer(response)
            return Response(serializer.data)
        return Response(status=404)
