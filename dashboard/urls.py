from django.urls import path
from .views import ItemDashboardView

urlpatterns = [
    path('items/', ItemDashboardView.as_view(), name='item_dashboard'),
]
