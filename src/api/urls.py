from django.urls import include, path
from . import views

urlpatterns = [
    path('health/', views.HealthView.as_view(), name='health'),
    path('v1/', include('src.api.v1.urls'))
]
