from django import forms

#class

class loginforms(forms.Form):
    username = forms.CharField()
    password = forms.CharField()