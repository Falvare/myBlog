from django.urls import path
from .views import ArticleList, ArticleDetails

urlpatterns = [
    path('', ArticleList.as_view(), name='articles'),
    path('article/<slug:slug>/', ArticleDetails.as_view(), name='article details')
]
