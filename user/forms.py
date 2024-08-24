from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Profile

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username' , 'password1' , 'password2')

    
    def __init__(self,*args,**kwargs):
        super(RegisterUserForm , self).__init__(*args , **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

class UpdateUserForm(forms.ModelForm):
    username= forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['username']
class UpdateProfileForm(forms.ModelForm):
    avatar= forms.ImageField(required=False,widget=forms.FileInput(attrs={'class':'form-control'}))

    class Meta:
        model = Profile
        fields = ['avatar']