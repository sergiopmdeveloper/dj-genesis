from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django_htmx.http import HttpResponseClientRefresh


def home(request: HttpRequest) -> HttpResponse:
    """
    The home view

    Parameters
    ----------
    request : HttpRequest
        The request object

    Returns
    -------
    HttpResponse
        The rendered home page
    """

    if request.htmx:
        print("htmx is working!")
        return HttpResponseClientRefresh()

    return render(request, "base/home.html")
