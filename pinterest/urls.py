








from django.urls import path

from .views import home, Search

app_name = 'pinterest'

urlpatterns = [
    path('', home, name='home'),
    path('search/', Search.as_view(), name='search'),
]