from django.urls import path
from .views import DenguaCaseManagementView,AddressView
urlpatterns = [
   path('case/', DenguaCaseManagementView.as_view(), name='dengua_case_manage'),
   path('address/', AddressView.as_view(), name='address_view'),
]

