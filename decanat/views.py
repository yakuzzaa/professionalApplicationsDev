from django.shortcuts import render, redirect
from decanat import models
from decanat import forms

# Create your views here.

def viewbd(request):
    spravki = models.Spravka.objects.all()
    if request.method == "GET":
        f = forms.Add()
        return render(request, "decanat/index.html", {"spravki": spravki, "f": f})

    if request.method == "POST":
        f = forms.Add(request.POST)
        f.save()
        return redirect("bd")





