from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django_htmx.http import HttpResponseClientRefresh


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

    if request.method == "POST" and request.htmx:
        email = request.POST.get("email")
        password = request.POST.get("password")

        errors = []

        if not email:
            errors.append("Email is required")

        if not password:
            errors.append("Password is required")

        if errors:
            return render(request, "form-errors.html", {"errors": errors})

        return HttpResponseClientRefresh()

    return render(request, "auth/sign-in.html")
