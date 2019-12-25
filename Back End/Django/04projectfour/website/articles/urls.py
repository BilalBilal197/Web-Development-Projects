
from django.urls import path, include

from . import views

urlpatterns = [
    
    path('', views.ArticleListView.as_view(), name='home'),
    path('artcle/<int:pk>', views.ArticleDetailView.as_view(), name='article_page'),
]

