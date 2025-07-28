from django.urls import path
from . import views

urlpatterns = [
    path('create-checkout-session/', views.CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
]