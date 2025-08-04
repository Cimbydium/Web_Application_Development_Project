from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Recipe, Review

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'creator', 'category', 'prep_time', 'instructions', 'image']
        
        labels = {
            'title': 'Recipe Title',
            'creator': 'Recipe Creator',
            'category': 'Category',
            'prep_time': 'Preparation Time (minutes)',
            'instructions': 'Recipe Instructions',
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write your review...'}),
        }       
