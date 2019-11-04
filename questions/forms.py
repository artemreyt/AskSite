from django import forms
from .models import Question


# class QuestionForm(forms.ModelForm):
#     title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Напишите здесь название',
#                                                           'width': 300}))

#     class Meta:
#         model = Question
#         fields = ['title', 'text', 'photo']

class AskForm(forms.Form):
    title = forms.CharField(label='Название:', max_length=255)
    text = forms.CharField(label="Описание:", widget=forms.Textarea)
    photo = forms.ImageField(label="Вставьте фотографию:", required=False)

    def clean(self):
        title = self.data['title']
        text = self.data['text']

        if len(title.split()) >= len(text.split()):
            raise forms.ValidationError(
                u'Описание не может быть меньше, чем название!')

    def clean_title(self):
        title = self.cleaned_data['title']


        if len(title.split()) < 3:
            raise forms.ValidationError(
                u'В названии должно быть не меньше 3х слов!')
        return title

    def clean_text(self):
        text = self.cleaned_data['text']
        if len(text.split()) < 10:
            raise forms.ValidationError(
                u'В описании должно быть не меньше 10 слов')
        return text

    def save(self):
        print(self.data)
        question = Question(**self.cleaned_data)
        question.save()
        return question

