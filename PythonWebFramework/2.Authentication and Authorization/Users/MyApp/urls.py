from django.urls import path
from Users.MyApp import views


urlpatterns = [
    path('', views.index, name='index'),
    path('details/', views.details, name='details'),
    path('details-logout/', views.details_logout, name='logout'),
    path('log1/', views.login_required, name='log1'),
    path('log2/', views.LoginRequired.as_view(), name='log2'),
    path('login/', views.log_in, name='login'),
    path('info/', views.info, name='information')
]
