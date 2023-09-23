from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from GameStats.Games import views


urlpatterns = [
    path('create/', views.CreateGame.as_view(), name='create game'),
    path('all/games/', views.GamesView.as_view(), name='all-games'),
    path('game/<int:pk>/details/', views.game_details, name='game-details'),
    path('game/<int:pk>/edit/', views.EditGame.as_view(), name='edit-game'),
    path('game/<int:pk>/delete/', views.DeleteGame.as_view(), name="delete-game"),
    path('game/<int:pk>/comment/', views.comment_game, name='add-comment'),
    path('game/<int:pk>/edit/comment/', views.EditComment.as_view(), name='edit-comment'),
    path('game/<int:pk>/comment/delete/', views.DeleteComment.as_view(), name="delete-comment"),
    path('game/<str:game>/all/comments/', views.comments, name='comments')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
