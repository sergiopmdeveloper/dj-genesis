from django.urls import path

from auth.views import sign_in, sign_up

urlpatterns = [
    path("sign-in", sign_in, name="sign-in"),
    path("sign-up", sign_up, name="sign-up"),
]
