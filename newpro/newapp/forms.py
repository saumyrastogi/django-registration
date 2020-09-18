from django import forms
from django.contrib.auth.models import User
from newapp.models import UserProfileInfo

class UserForm(forms.ModelForm):
    def start_with_upper(value):
        if value[0]!=value[0].upper():
            raise forms.ValidationError("FIRST LETTER SHOULD START WITH UPPER CASE")
    password = forms.CharField(widget=forms.PasswordInput())
    username = forms.CharField(validators=[start_with_upper])
    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields=('portfolio_site','profile_pic')
