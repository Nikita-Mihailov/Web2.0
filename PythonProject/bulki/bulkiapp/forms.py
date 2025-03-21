# forms.py
from django import forms
from django.forms import ModelForm

from .models import Comment, Article


class FeedbackForm(forms.Form):
    name = forms.CharField(label="Ваше имя", max_length=100, widget=forms.TextInput(attrs={'class': 'input-field'}))
    email = forms.EmailField(label="Ваш email", widget=forms.EmailInput(attrs={'class': 'input-field'}))
    rating = forms.ChoiceField(label="Оценка сайта", choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], widget=forms.RadioSelect)
    usability = forms.ChoiceField(label="Удобство использования", choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], widget=forms.Select(attrs={'class': 'input-field'}))
    design = forms.ChoiceField(label="Дизайн сайта", choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], widget=forms.Select(attrs={'class': 'input-field'}))
    comments = forms.CharField(label="Ваши пожелания", widget=forms.Textarea(attrs={'class': 'input-field'}))
    subscribe = forms.BooleanField(label="Подписаться на рассылку", required=False, widget=forms.CheckboxInput(attrs={'class': 'input-field'}))


class CommentModelForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]

    def __init__(self, *args, **kwargs):
        super(CommentModelForm, self).__init__(*args, **kwargs)
        self.fields["text"].help_text = ""
        self.fields["text"].label = ""
        self.fields["text"].widget = forms.Textarea(
            attrs={
                "placeholder": "Текст комментария",
                "rows": 1,
                "class": "form-control",
            }
        )

class BlogForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'summary', 'content', 'image']