from django.shortcuts import HttpResponse, render
from tution.models import Contact

def home (request):
    name_list1 = ['Rafsan','Ahmed','Swadhin']
    name_list2 = ['Feroz','Akash','Sakib']
    name_list3 = ['Pappu','Fahim','Emon']
    context = {
        'name_1' : name_list1,
        'name_2' : name_list2,
        'name_3' : name_list3,
    }
    #return HttpResponse("Hello World")
    return render(request, 'home.html',context)

#12 no video
'''
def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['phone']
        content = request.POST['content']
        obj = Contact(name = name, phone = phone, content = content)
        obj.save()
      
    return render(request,'contact.html')

'''
