from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from GameStats.Games.forms import GameForm, CommentGameForm
from GameStats.Games.generators import game_rating_generator
from GameStats.Games.models import Game, Comment


class CreateGame(LoginRequiredMixin, CreateView):
    template_name = "Games/create-game.html"
    form_class = GameForm
    success_url = reverse_lazy('all-games')

    def get(self, request, *args, **kwargs):
        if not request.user.is_staff and not request.user.is_superuser:
            return redirect("no-access")
        return super().get(request, *args, **kwargs)

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields['creator'].initial = self.request.user.get_username()
        return form


class GamesView(ListView):
    template_name = "Games/all-games.html"
    model = Game
    context_object_name = "games"


def game_details(request, pk):
    game = Game.objects.get(pk=pk)
    context = {
        "game": game,
        "rating": game_rating_generator(game.title)
    }
    return render(request, "Games/details.html", context)


class EditGame(LoginRequiredMixin, UpdateView):
    template_name = "Games/edit-game.html"
    form_class = GameForm
    model = Game
    context_object_name = "game"
    success_url = reverse_lazy("all-games")

    def get(self, request, *args, **kwargs):
        self.extra_context = {"user": self.request.user.get_username()}
        return super().get(request, *args, **kwargs)

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields['creator'].initial = self.request.user.get_username()
        return form


class DeleteGame(LoginRequiredMixin, DeleteView):
    template_name = "Games/delete-game.html"
    model = Game
    context_object_name = "game"
    success_url = reverse_lazy("all-games")

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.delete()
        for comment in Comment.objects.filter(game=self.object.title):
            comment.delete()
        return HttpResponseRedirect(success_url)


@login_required
def comment_game(request, pk):
    game = Game.objects.get(pk=pk)

    comment_form = CommentGameForm(request.POST or None)

    comment_form.fields["game"].initial = game.title
    comment_form.fields["creator"].initial = request.user.get_username()

    context = {
        "game": game,
        "form": comment_form,
        'pk': pk,
    }

    if comment_form.is_valid():
        comment_form.save()
        return redirect("game-details", pk=game.id)

    return render(request, "Games/add-comment.html", context)


def comments(request, game):
    all_comments = Comment.objects.filter(game=game).order_by("-rating")

    return render(request, "Games/comments.html", {"comments": all_comments, "game": game})


class EditComment(LoginRequiredMixin, UpdateView):
    model = Comment
    template_name = "Games/edit-comment.html"
    form_class = CommentGameForm
    success_url = reverse_lazy("all-games")


class DeleteComment(LoginRequiredMixin, DeleteView):
    template_name = "Games/delete-comment.html"
    model = Comment
    context_object_name = "comment"
    success_url = reverse_lazy("all-games")

