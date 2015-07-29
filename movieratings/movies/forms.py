from django import forms
from django.contrib.auth.models import User
from .models import Rating


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)


class RatingForm(forms.ModelForm):
    RATING_CHOICES = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5))

    rating = forms.ChoiceField(choices=RATING_CHOICES,
                               label="Rating",
                               required=True)
    class Meta:
        model = Rating
        fields = ('rating',)

class EditForm(forms.ModelForm):
    RATING_CHOICES = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5))

    rating = forms.ChoiceField(choices=RATING_CHOICES,
                               label="Rating",
                               required=True)


    class Meta:
        model = Rating
        fields = ('rating',)


