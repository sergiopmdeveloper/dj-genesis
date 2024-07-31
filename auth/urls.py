from django.urls import path

from auth.views import sign_in

urlpatterns = [
    path("sign-in", sign_in, name="sign-in"),
]
