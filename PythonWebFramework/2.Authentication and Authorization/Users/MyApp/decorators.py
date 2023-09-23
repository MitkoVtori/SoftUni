from django.http import HttpResponse


def allowed_groups(groups=[]):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return HttpResponse("Not authenticated!")

            if request.user.is_superuser:
                return view_func(request, *args, **kwargs)

            user_groups = request.user.groups.filter(name__in=groups)

            if not user_groups:
                return HttpResponse("You do not have access to this page!")

            return view_func(request, *args, **kwargs)

        return wrapper

    return decorator
