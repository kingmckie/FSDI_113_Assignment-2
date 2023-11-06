from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy



classs SignUpView(CreateView)
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy ("login")