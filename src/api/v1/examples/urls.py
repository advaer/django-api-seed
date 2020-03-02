from django.urls import path

from . import views

urlpatterns = [
    path('farms/', views.FarmListView.as_view(), name='farm-list'),
    path('farms/<int:pk>/', views.FarmView.as_view(), name='farm'),

    path('fields/', views.FieldListView.as_view(), name='field-list'),
    path('fields/<int:pk>/', views.FieldView.as_view(), name='field'),

    path('farms/fields/', views.FarmFieldsListView.as_view(), name='farm-fields-list'),
    path('farms/<int:pk>/fields/', views.FarmFieldsView.as_view(), name='farm-fields'),
]
