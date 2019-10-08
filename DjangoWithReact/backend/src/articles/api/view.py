from rest_framework.generics import ListAPIView,RetrieveAPIView
from articles.models import Article
from .serialzers import ArticleSerializer


class ArticleListView (ListAPIView):   #getall
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetailView (RetrieveAPIView): #getOne
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


