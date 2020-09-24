from django.conf import settings
from django.contrib import admin
from django.urls import path
from .views import *
from django.conf.urls.static import static

app_name = 'mybooks'

urlpatterns = [
                  path('', index, name='index'),
                  path('/<int:pk>/', BookDetail.as_view(), name='book_detail'),
                  path('/author/<int:pk>/', authorDetail, name='author_detail'),
                  path('/search/', SearchResult.as_view(), name='search_detail'),
                  path('/add_book/', addBookPage, name='add_book_page'),
                  path('/delete/<int:pk>/', delete_book, name='delete_book')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
