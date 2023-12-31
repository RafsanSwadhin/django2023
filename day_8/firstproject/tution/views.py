from django.shortcuts import render
from .models import Contact
from .forms import ContactForm

# Create your views here.

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
         # just write this 
         # form.save() .....this is the another way to create a form
         name = request.POST['name']
         phone = request.POST['phone']
         content = request.POST['content']
         obj = Contact(name = name, phone = phone, content = content)
         obj.save()
    else:
        form = ContactForm()
    return render(request,'contact.html',{'form':form})