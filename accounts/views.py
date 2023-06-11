from django.views.generic import TemplateView, CreateView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy


class HomePageView(TemplateView):
    template_name = 'home.html'


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('home')


