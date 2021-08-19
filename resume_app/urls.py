from django.urls import path
from .views import index, thanks


urlpatterns = [
    path('', index, name="home"),
    path('thanks', thanks, name='thanks')
]


