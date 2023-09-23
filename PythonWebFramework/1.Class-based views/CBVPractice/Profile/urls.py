from django.urls import path
from CBVPractice.Profile import views
from django.views.generic import RedirectView


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('home/', RedirectView.as_view(url='http://localhost:8000/')),
    path('articles/', views.ArticleListView.as_view(), name='articles'),
    path('details/<pk>/', views.ArticleDetailView.as_view(), name='details'),
    path('create/', views.CreateArticle.as_view(), name='create'),
    path('update/<pk>/', views.UpdateArticle.as_view(), name='update'),
    path('delete/<pk>/', views.ArticleDeleteView.as_view(), name='delete')
]
