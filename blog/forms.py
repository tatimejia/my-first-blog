from django import forms

from .models import Post

class PostForm(forms.ModelForm): #nombre del formulario PostForm

    class Meta:
        model = Post  #use el modelo Post para el formulario
        fields = ('title', 'text',)