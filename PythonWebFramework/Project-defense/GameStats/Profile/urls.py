from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from GameStats.Profile import views


urlpatterns = [
    path('register/', views.CreateUser.as_view(), name="register"),
    path('login/', views.UserLogin.as_view(), name="login"),
    path('@me/logout/', views.LogoutPageView.as_view(), name='logout'),
    path('@me/logout/action/', views.UserLogout.as_view(), name='logout-action'),
    path('@me/', views.UserDetails.as_view(), name='user'),
    path('@me/edit/', views.EditUser.as_view(), name='edit-user'),
    path('@me/edit/change/password/', views.ChangeUserPassword.as_view(), name='change-password'),
    path('@me/details/security/account/delete/', views.DeleteUser.as_view(), name='delete-user')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
