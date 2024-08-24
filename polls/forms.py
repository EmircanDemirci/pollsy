from django import forms

from .models import Question,Choice


class CreateQuestionForm(forms.ModelForm):
    question_text = forms.CharField(max_length=200 , widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model=Question
        fields = ('question_text',)

class CreateChoiceForm(forms.ModelForm):
    class Meta:
        model=Choice
        fields = ['choice_text']
