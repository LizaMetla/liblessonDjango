from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import TemplateView

from core.forms import GenreForm
from mixins.auth import AbsLoginMixin


class GenreCreateView(AbsLoginMixin, TemplateView):
    template_name = 'core/genre-create.html'

    def get_context_data(self, **kwargs):
        context = super(GenreCreateView, self).get_context_data(**kwargs)
        context['form'] = GenreForm(self.request.POST or None, self.request.FILES or None)
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        if context['form'].is_valid():
            genre = context['form'].save()
            return redirect(reverse('index'))
        else:
            return render(request, self.template_name, context)