from rest_framework import viewsets,permissions
from rest_framework.permissions import IsAuthenticated

from articles.models import Article
from .serialzers import ArticleSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    permission_classes = [
        IsAuthenticated
    ]
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    

# from rest_framework.generics import (
#     ListAPIView,
# CreateAPIView,
# RetrieveAPIView,
# UpdateAPIView,
# DestroyAPIView) 


# class ArticleListView (ListAPIView):   #getall
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer


# class ArticleDetailView (RetrieveAPIView): #getOne
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

# class ArticleCreateView (CreateAPIView): #create
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

# class ArticleUpdateView (UpdateAPIView): #update
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

# class ArticleDeleteView (DestroyAPIView): #delete
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer


