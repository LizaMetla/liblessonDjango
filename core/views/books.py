from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView, TemplateView

from core.forms import BookForm
from core.models import Book
from mixins.auth import AbsLoginMixin


class DetailBookView(DetailView):
    template_name = 'core/detail-book.html'
    model = Book


class BookCreateView(AbsLoginMixin, TemplateView):
    template_name = 'core/book-create.html'

    def get_context_data(self, **kwargs):
        context = super(BookCreateView, self).get_context_data(**kwargs)
        context['form'] = BookForm(self.request.POST or None, self.request.FILES or None)
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        if context['form'].is_valid():
            book = context['form'].save()
            return redirect(reverse('detail_book', kwargs={'pk':book.pk}))
        else:
            return render(request, self.template_name, context)


class BookDeleteView(AbsLoginMixin, View):

    def get(self, request, *args, **kwargs):
        book_pk = kwargs.get('pk')
        book = get_object_or_404(Book, pk=book_pk)
        book.delete()
        return redirect(reverse('index'))