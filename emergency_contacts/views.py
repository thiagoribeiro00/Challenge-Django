from django.shortcuts import render, redirect
from .models import Contact
from .serializers import ContactSerializer

# Home View
def home(request):
    return render(request, 'emergency_contacts/home.html')

# Create Contact View
def create_contact(request):
    if request.method == 'POST':
        serializer = ContactSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return redirect('home')
    return render(request, 'emergency_contacts/create_contact.html')

# Delete Contact View
def delete_contact(request):
    if request.method == 'POST':
        contact_id = request.POST.get('contact_id')
        try:
            contact = Contact.objects.get(id=contact_id)
            contact.delete()
            return redirect('home')
        except Contact.DoesNotExist:
            # Handle the error if contact does not exist
            pass
    return render(request, 'emergency_contacts/delete_contact.html')
