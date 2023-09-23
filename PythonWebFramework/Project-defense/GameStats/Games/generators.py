from GameStats.Games.models import Comment


def game_rating_generator(game_title):
    all_ratings = Comment.objects.filter(game=game_title)
    try:
        return f"{(sum([rating.rating for rating in all_ratings]) / len(all_ratings)):.2f}"
    except ZeroDivisionError:
        return "---"

