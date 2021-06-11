from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView

from core.forms import LoginForm, UserRegistrationForm
from core.utils.logs import log_record


class LoginView(TemplateView):
    template_name = 'core/login.html'

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        context['form'] = LoginForm(self.request.POST or None)
        log_record(self.request, 'auth', f'Move to login page, method: {self.request.method}')
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        if context['form'].is_valid():
            username = context['form'].cleaned_data.get("username")
            password = context['form'].cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            login(request, user)
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            return redirect(reverse('index'))
        return render(request, self.template_name, context)


class RegisterView(TemplateView):
    template_name = 'core/registration.html'

    def post(self, request, *args, **kwargs):
        log_record(request, 'registrations', 'User reg in system')
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'core/registration-done.html', {'new_user': new_user})

        return render(request, self.template_name, {'user_form': user_form})