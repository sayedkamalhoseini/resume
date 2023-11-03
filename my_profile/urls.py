from django.contrib import admin
from django.urls import include, path

from my_profile.views import index_view

urlpatterns = [
    path('', index_view ),
]
