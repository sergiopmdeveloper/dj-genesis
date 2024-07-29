from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django_htmx.http import HttpResponseClientRefresh


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

    if request.htmx:
        return HttpResponseClientRefresh()

    return render(request, "auth/sign-in.html")
