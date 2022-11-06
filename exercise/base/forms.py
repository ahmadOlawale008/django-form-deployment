from . models import UserProfile
from django import forms
from django.contrib.auth.models import User
from django.core import validators
class UserProfileForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    rep_password = forms.CharField(widget=forms.PasswordInput, label = 'Confirm your password')
    botcatcher = forms.CharField(widget=forms.HiddenInput, required=False)
    def catch_bot(self):
        botcatcher = self.cleaned_data['botcatcher']
        if len(botcatcher) > 0:
            raise forms.ValidationError('Bot error!!!')
        return botcatcher
    def clean(self):
        all_clean = super().clean()
        password = all_clean['password']
        email = all_clean['email']
        rep_password = all_clean['rep_password']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email already exists')
        if password != rep_password:
            raise forms.ValidationError('Please ensure that your password are same')  

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfile(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('portfolio_site', 'profile_pic')
        
        
