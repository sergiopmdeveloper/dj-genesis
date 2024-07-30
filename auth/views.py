from django.contrib.auth import authenticate, login
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.cache import never_cache
from django.views.decorators.http import require_http_methods
from django_htmx.http import HttpResponseClientRedirect


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
        username = request.POST.get("username")
        password = request.POST.get("password")

        errors = []

        if not username:
            errors.append("Username is required")

        if not password:
            errors.append("Password is required")

        if errors:
            return render(request, "form-errors.html", {"errors": errors})

        user = authenticate(request, username=username, password=password)

        if not user:
            errors.append("Invalid username or password")

            return render(request, "form-errors.html", {"errors": errors})

        login(request, user)

        return HttpResponseClientRedirect("/")

    from_redirection = bool(request.GET.get("next"))

    return render(request, "auth/sign-in.html", {"from_redirection": from_redirection})
