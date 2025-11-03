# forms.ModelForm → a Django form automatically tied to a model
# model = Post → tells Django which model to create an instance of
# fields = [...] → specify which fields should appear in the form

from django import forms
from .models import Post

# This form will let students create new Posts
class PostForm(forms.ModelForm):
    class Meta:
        # The model this form is based on
        model = Post
        # Fields the student can fill out
        fields = ['section', 'title', 'content']