from .views import TestView
from django.urls import path
urlpatterns = [
   path('my_test/', TestView.as_view(), name='my_test'),
]

