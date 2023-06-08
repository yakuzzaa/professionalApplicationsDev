from django import forms

from decanat.models import Spravka


class Add(forms.ModelForm):
    class Meta:
        model = Spravka
        fields = ["fio", "grant", "destination"]
