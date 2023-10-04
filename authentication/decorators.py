from django.shortcuts import redirect


def if_not_logged_in(redirect_to):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            if request.user.is_authenticated:
                return redirect(redirect_to)
            else:
                return view_func(request, *args, **kwargs)
        return wrapper_func
    return decorator
