from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, DetailView

from core.forms import AuthorForm
from core.models import Author
from mixins.auth import AbsLoginMixin


class AuthorsView(TemplateView):
    template_name = 'core/authors.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['authors'] = Author.objects.all()

        return render(request, self.template_name, context)


class AuthorDetailView(DetailView):
    template_name = 'core/author-detail.html'
    model = Author


class AuthorCreateView(AbsLoginMixin, TemplateView):
    template_name = 'core/create-author.html'

    def get_context_data(self, **kwargs):
        context = super(AuthorCreateView, self).get_context_data(**kwargs)
        context['form'] = AuthorForm(self.request.POST or None, self.request.FILES or None)
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        if context['form'].is_valid():
            author = context['form'].save()
            return redirect(reverse('detail_author', kwargs={'pk': author.pk}))
        else:
            return render(request, self.template_name, context)


class AuthorDeleteView(AbsLoginMixin, View):
    def get(self, request, *args, **kwargs):
        author_pk = kwargs.get('pk')
        author = get_object_or_404(Author, pk=author_pk)
        author.delete()
        return redirect(reverse('index'))