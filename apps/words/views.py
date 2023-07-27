from typing import Any, Dict

from django.db.models.query import QuerySet
from .models import Unit, Text
from django.shortcuts import render
from django.views.generic import ListView, DetailView


class UnitListView(ListView):
    model = Unit
    template_name = "units.html"


class OneUnitTexts(DetailView):
    model = Unit
    template_name = "one_unit_texts.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['texts'] = context['unit'].texts.all()
        return context


class TextsView(ListView):
    paginate_by = 1
    model = Text
    template_name = "one_text.html"
    context_object_name = 'text'
    # paginate_orphans = 3

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['current_page'] = context.pop('page_obj')
        return context
        
    def get_queryset(self) -> QuerySet[Any]:
        unit_id = self.kwargs['unit_id']
        texts = Text.objects.filter(unit_id=unit_id)
        return texts