from django.forms import ModelForm
from .models import Book


class CreateBookForm(ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'pub_date',
            'description',
            'image',
            'author_name'
        ]
