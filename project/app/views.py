from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import *

# Create your views here.
def appdisplay(request):
    return HttpResponse("app msg")

def showall(request):
    query=Details.objects.all()
    return render(request,'show.html',{'query':query})


def delete_detail(request, id):
    detail = get_object_or_404(Details, id=id)
    detail.delete()
    return redirect('showall')

def add(request):
    if request.method=="POST":
        Name=request.POST.get('Name')
        FirstName=request.POST.get('FirstName')
        Email=request.POST.get('Email')
        PhoneNumber=request.POST.get('PhoneNumber')
        Gender=request.POST.get('Gender')

        query=Details(Name=Name,FirstName=FirstName,Email=Email,PhoneNumber=PhoneNumber,Gender=Gender)
        query.save()

        return redirect(showall)
    
    return render(request,'insert.html',)





def update_detail(request, id):
    detail = get_object_or_404(Details, id=id)

    if request.method == 'POST':
        detail.Name = request.POST.get('Name')
        detail.FirstName = request.POST.get('FirstName')
        detail.Email = request.POST.get('Email')
        detail.PhoneNumber = request.POST.get('PhoneNumber')
        detail.Gender=request.POST.get('Gender')
        detail.save()
        return redirect('showall')
    
    return render(request, 'update.html', {'detail': detail})






















































































