from django import forms
from .models import Question


class QuestionForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Напишите здесь название',
                                                          'width': 300}))

    class Meta:
        model = Question
        fields = ['title', 'text', 'photo']