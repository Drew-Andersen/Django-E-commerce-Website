from django.shortcuts import render
from django.views.generic import View, TemplateView

# Create your views here.
class IndexView(TemplateView):
    template_name = 'shop_app/shop_index.html'

class TestView(TemplateView):
    template_name = 'shop_app/test.html'