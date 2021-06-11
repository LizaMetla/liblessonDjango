import abc

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class AbsLoginMixin(LoginRequiredMixin, metaclass=abc.ABCMeta):
    login_url = reverse_lazy('login')
