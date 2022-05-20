from django import forms
from django.http import HttpResponse

class InputTask(forms.Form):
   def list():
        task = forms.CharField(max_length=1000)
        #status = forms.CharField(max_length=1000)
        name = forms.CharField(required=False)

