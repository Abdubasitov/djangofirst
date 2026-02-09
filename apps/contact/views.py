from django.shortcuts import render, get_object_or_404
from .models import ContactPage

def contacts(request):
    contact_page = ContactPage.objects.first()
    return render(request, "page/contact.html", {"contact_page": contact_page})
