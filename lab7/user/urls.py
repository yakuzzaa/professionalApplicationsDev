from django.urls import path

from . import views

urlpatterns = [
    path("login/", views.LoginUser.as_view()),
    path("signup/", views.SignUP.as_view()),

]
