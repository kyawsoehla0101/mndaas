from django.forms import forms,ModelForm
from base.models import *

class PostCreateFrom(ModelForm):
    class Meta:
        model=Post
        fields='__all__'


