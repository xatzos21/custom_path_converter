from django.urls import path, register_converter
from customers.views import index, validate_phone1
from customers.converts import PhoneNumberConverter

register_converter(PhoneNumberConverter, "phone")

urlpatterns = [
    path("", index),
    path("customers/phone/<phone:phone_number>/", validate_phone1),
]