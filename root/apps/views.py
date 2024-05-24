from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import TemplateView, CreateView, ListView
from .models import Home, Product, About, contacts
from .forms import SignupForm, LoginForm, ContactForm
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = SignupForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)
        if user:
            login(self.request, user)
            return super().form_valid(form)
        else:
            form.add_error(None, 'Invalid username or password')
            return self.form_invalid(form)


class HomeView(ListView):
    model = Home
    template_name = 'home.html'
    context_object_name = 'homes'
    success_url = '/'


class AboutView(ListView):
    model = About
    template_name = 'about.html'
    context_object_name = 'abouts'


def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'contact.html', context=context)


class ProductView(ListView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'products'
