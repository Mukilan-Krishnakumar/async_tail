from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def health(request):
    return HttpResponse("OK")


def message_window(request):
    return render(request, "message_window.html")
