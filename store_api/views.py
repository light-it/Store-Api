from store_api.models import Category, Item
from store_api.serializers import CategorySerializer, ItemSerializer
from store_api.serializers import ItemListSerializer
from django.shortcuts import render
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework import viewsets
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
        serializer = ItemListSerializer(response, many=True)
        return Response(serializer.data)


class ItemDetailView(APIView):

    def get(self, request, pk):
        if Item.objects.filter(pk=pk).exists():
            response = Item.objects.get(pk=pk)
            serializer = ItemSerializer(response)
            return Response(serializer.data)
        return Response(status=404)


class ItemAddView(APIView):

    def post(self, request, format=None):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class CategoryAddView(APIView):

    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
