from django import forms
from .models import Category, Post


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]
        labels = {"name": "Название категории"}
    


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "description", "image", "category"]
        labels = {
            "title": "Название",
            "description": "Описание",
            "image": "Изображение",
            "category": "Категория",
        }