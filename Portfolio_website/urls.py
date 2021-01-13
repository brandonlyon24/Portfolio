from django.urls import path
from . import views

urlpatterns = [
    path('portfolio_home', views.portfolio_home, name='portfolio_home'),
]