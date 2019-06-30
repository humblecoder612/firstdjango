from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from django.contrib.auth.models import User

class Newform(UserCreationForm):
    email=forms.EmailField(required=True)

    class Meta:
        model=User
        fields=("username","email","password1","password2")

    def save(self,commit=True):
        user=super(Newform,self).save(commit=False)
        user.email=self.cleaned_data.get("username")
        if  commit:
            user.save()
        return user
