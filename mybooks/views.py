from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import Q
import request
from django.urls import reverse
from .forms import CreateBookForm
from .models import Book, Author
from django.contrib.auth.mixins import LoginRequiredMixin


class BookList(ListView):
    model = Book
    template_name = 'mybooks/index.html'


def index(request):
    get_book = Book.objects.all()
    return render(request, 'mybooks/index.html', {'book': get_book, 'django': 'active'})


class BookDetail(DetailView):
    model = Book
    template_name = 'mybooks/book_detail.html'


def authorDetail(request, pk):
    author = Author.objects.get(pk=pk)
    context = Book.objects.filter(author_name=pk)
    return render(request, 'mybooks/author_detail.html', {'author': author, 'books': context})


class SearchResult(ListView):
    model = Book
    template_name = 'dediluk/search.html'

    def get_queryset(self):
        query = self.request.GET.get('search')
        object_list = Book.objects.filter(Q(title__icontains=query.lower()) | Q(title__icontains=query.title()))
        return object_list


def addBookPage(request):
    form = CreateBookForm(request.POST, request.FILES or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("mybooks:index"))
    return render(request, 'mybooks/add_book.html', {'form': form})


def addingBook(request):
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

    # print(Book.author_name.set())
    book = Book(title=request.POST.get('title'), pub_date=request.POST.get('pub_date'),
                description=request.POST.get('description'),
                image=request.POST.get('image'), author_name=set(Author.objects.all()))
    print(book.title)
    print('=========================================================')
    book.save()
    return render(request, 'mybooks/index.html')


def delete_book(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    get_book = Book.objects.all()
    return render(request, 'mybooks/index.html', {'book': get_book})
# description,image,author_name
