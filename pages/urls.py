# django
from django.urls import path

# local
from .views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home')
]
