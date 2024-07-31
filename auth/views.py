from django.contrib.auth import login
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.cache import never_cache
from django.views.decorators.http import require_http_methods
from django_htmx.http import HttpResponseClientRedirect

from auth.utils.sign_in import SignInHandler


@never_cache
@require_http_methods(["GET", "POST"])
def sign_in(request: HttpRequest) -> HttpResponse:
    """
    The sign in view

    Parameters
    ----------
    request : HttpRequest
        The request object

    Returns
    -------
    HttpResponse
        The rendered sign in page
    """

    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST" and request.htmx:
        sign_in_handler = SignInHandler(
            request=request,
            username=request.POST.get("username"),
            password=request.POST.get("password"),
        )

        sign_in_handler.validate_data()

        if sign_in_handler.invalid:
            return render(
                request, "form-errors.html", {"errors": sign_in_handler.errors}
            )

        sign_in_handler.validate_user()

        if sign_in_handler.invalid:
            return render(
                request, "form-errors.html", {"errors": sign_in_handler.errors}
            )

        login(request, sign_in_handler.user)

        return HttpResponseClientRedirect("/")

    from_redirection = bool(request.GET.get("next"))

    return render(request, "auth/sign-in.html", {"from_redirection": from_redirection})


@never_cache
@require_http_methods(["GET", "POST"])
def sign_up(request: HttpRequest) -> HttpResponse:
    """
    The sign up view

    Parameters
    ----------
    request : HttpRequest
        The request object

    Returns
    -------
    HttpResponse
        The rendered sign up page
    """

    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST" and request.htmx:
        return render(request, "form-errors.html", {"errors": ["Not implemented..."]})

    return render(request, "auth/sign-up.html")
