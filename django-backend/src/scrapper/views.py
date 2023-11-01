from django import views
from django.shortcuts import render
from rest_framework import generics, viewsets
from .serializers import ArticleSerializer
from .models import Article
from rest_framework.views import APIView
from rest_framework.response import Response

from . import tasks





class ScrapperAPIView(APIView):

    
    def get(self,request):
        tasks.parse_all.delay()
        return Response({'status':'OK',})


#class ScrapperAPIView(generics.ListAPIView):
#    queryset = Article.objects.all()
#    serializer_class = ArticleSerializer
#
#class ArticleViewSet(views.ModelViewSet):
#    pass