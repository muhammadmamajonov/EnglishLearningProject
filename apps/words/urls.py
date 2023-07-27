from .views import *
from django.urls import path

urlpatterns = [
    path('units', UnitListView.as_view(), name='units'),
    path('one-unit-texts/<int:pk>', OneUnitTexts.as_view(), name='one_unit_texts'),
    path('<int:unit_id>/', TextsView.as_view(), name='texts')
]