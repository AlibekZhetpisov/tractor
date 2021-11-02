from django import forms

from webapp.models import Order, Comment, Technique


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ["technique", "author"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ["technique", "author"]


class TechniqueStatusForm(forms.ModelForm):
    class Meta:
        model = Technique
        exclude = ["advertiser", "category", "name", "foto", "price", "price_description", "description", "sale_price", "qty"]



class SearchForm(forms.Form):
    q = forms.CharField(max_length=100, required=False, label="Поиск")