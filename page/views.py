from django.shortcuts import render


# Create your views here.
from django.views.generic import TemplateView

from page.models import Category


class CategoryListView(TemplateView):
    template_name = 'index2.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        context['categories'] = categories
        return context
