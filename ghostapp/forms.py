from django import forms
from ghostapp.models import GPost

class PostForm(forms.Form):
    is_boast = forms.BooleanField(required=False)
    post_text = forms.CharField(max_length=280)
