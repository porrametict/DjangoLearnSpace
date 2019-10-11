from articles.api.view import ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', ArticleViewSet, basename='articles')
urlpatterns = router.urls


# from django.urls import path
# from .view import (ArticleListView,
# ArticleDetailView ,
# ArticleCreateView,
# ArticleUpdateView,
# ArticleDeleteView
#  )

# urlpatterns = [
#     path('',ArticleListView.as_view()),
#     path('create/',ArticleCreateView.as_view()),
#     path('<pk>',ArticleDetailView.as_view()),
#     path('<pk>/update/',ArticleUpdateView.as_view()),
#     path('<pk>/delete/',ArticleDeleteView.as_view()),

# ]