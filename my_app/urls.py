""

from django.urls import path

from my_app.views import index, albums

urlpatterns = [
    path('albums', albums),
    path('', index),
]
