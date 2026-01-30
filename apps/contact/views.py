from django.shortcuts import render, get_object_or_404
from .models import ContactPage

def contacts(request):
    contacts = get_object_or_404(ContactPage)
    return render(request, "page/contact.html", {"contact": contacts})
