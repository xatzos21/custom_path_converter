from django.shortcuts import render, HttpResponse
from django.http import JsonResponse

def index(request):
    return HttpResponse("Mediamarkt!")


def validate_phone1(request, phone_number):
    if len(phone_number) == 5:
        return JsonResponse({"error": "Invalid phone number"}, status=400)
    else:
        context = {'phone_number': phone_number}
        return render(request, "customers/phone_validation.html", context)
