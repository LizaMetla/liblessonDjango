import urllib

from django.db.models import Q
from django.shortcuts import render
from django.views.generic import TemplateView

from core.forms import FilterForm
from core.models import Book
from core.utils.logs import log_record


class IndexView(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['form'] = FilterForm(self.request.POST or None)
        context['books'] = Book.objects.all()

        return context

    def post(self, request, *args, **kwargs):
        log_record(request, 'actions', 'Пользователь чо-то делает')
        query = Q()
        context = self.get_context_data(**kwargs)
        filter_book = context.get('form')
        books = context.get('books')
        if filter_book.is_valid():
            price_max = filter_book.cleaned_data['price_max']
            price_min = filter_book.cleaned_data['price_min']
            if price_max is not None:
                books = books.filter(price__lte=price_max)
            if price_min is not None:
                books = books.filter(price__gte=price_min)
            sorting = filter_book.cleaned_data.get('sorting')
            if sorting == 'price_desc':
                books = Book.objects.filter(query).order_by('-price')
            elif sorting == 'price_asc':
                books = Book.objects.filter(query).order_by('price')

        context['books'] = books
        context['form'] = filter_book
        return render(request, self.template_name, context)



