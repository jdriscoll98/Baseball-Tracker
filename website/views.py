from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

# Application Views


# Home
class HomePageView(TemplateView):
    template_name = 'website/home_page.html'
