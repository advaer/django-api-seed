from django.urls import include, path

from src.api import views
from src.api.v1.examples.urls import urlpatterns as examples_urls

urlpatterns = [
    path('health/', views.HealthView.as_view(), name='health'),
    path('examples/', include(examples_urls))
]