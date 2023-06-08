from django.urls import path

from decanat import views

urlpatterns = [
    path("bd/", views.viewbd, name="bd")

]