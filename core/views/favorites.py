from django.db.models import Q
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView, TemplateView

from core.forms import BookForm
from core.models import Book
from mixins.auth import AbsLoginMixin



class AddToFavoriteView(View):
    def get(self, request, *args, **kwargs):
        book = get_object_or_404(Book, pk=kwargs.get('pk'))
        self.request.user.favorites.add(book)
        next_page = request.GET.get('next')
        if next_page:
            return HttpResponseRedirect(next_page)
        else:
            return redirect('index')

class RemoveFromFavoriteView(View):
    def get(self, request, *args, **kwargs):
        book = get_object_or_404(Book, pk=kwargs.get('pk'))
        self.request.user.favorites.remove(book)
        next_page = request.GET.get('next')
        if next_page:
            return HttpResponseRedirect(next_page)
        else:
            return redirect('index')

class FavoritesView(TemplateView):
    template_name = 'core/favorite-books.html'
    # context_object_name = 'books_list'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data( **kwargs)
        context['view_name'] = 'favourites'

        return context

    # def get_queryset(self):
    #     query = Q()
    #
    #     return self.request.user.favorites.filter(query)