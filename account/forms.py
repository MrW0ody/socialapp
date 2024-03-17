from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from account.models import Profile


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 != password2:
            raise forms.ValidationError("Passwords aren't the same")
        return password2

    def clean_email(self):
        email = self.cleaned_data['email']
        query = User.objects.exclude(id=self.instance.id).filter(email=email)
        if query.exists():
            raise forms.ValidationError(' Email already in use.')
        return email


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_email(self):
        email = self.cleaned_data['email']
        query = User.objects.exclude(id=self.instance.id).filter(email=email)
        if query.exists():
            raise forms.ValidationError(' Email already in use.')
        return email


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'follows', 'active']

