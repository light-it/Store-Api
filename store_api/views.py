from django.shortcuts import render
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response


class IndexView(View):

    def get(self, request):
        return render(request, 'index.html')
