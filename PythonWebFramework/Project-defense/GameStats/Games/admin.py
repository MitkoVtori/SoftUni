from django.contrib import admin
from GameStats.Games.models import Game, Comment


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = (
        "title", "creator", "genre"
    )
    list_display_links = ('title', 'creator', 'genre')

    list_filter = ("genre", "creator")

    def get_form(self, request, obj=None, *args, **kwargs):
        form = super(GameAdmin, self).get_form(request, *args, **kwargs)
        form.base_fields['creator'].initial = request.user
        form.base_fields['creator'].disabled = True
        form.base_fields['creator'].readonly = True
        return form

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        if obj is not None and obj.creator != request.user.get_username():
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        if obj is not None and obj.creator != request.user.get_username():
            return False
        return True


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("creator", "rating", "game", "id")

    list_filter = ("rating", "creator", "game", "id")

    def get_form(self, request, obj=None, *args, **kwargs):
        form = super(CommentAdmin, self).get_form(request, *args, **kwargs)
        form.base_fields['creator'].initial = request.user
        form.base_fields['game'].initial = Game.objects.first().title
        form.base_fields['creator'].disabled, form.base_fields['game'].disabled = True, True
        form.base_fields['creator'].readonly, form.base_fields['game'].readonly = True, True
        return form

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        if obj is not None and obj.creator != request.user.get_username():
            return False
        return True
