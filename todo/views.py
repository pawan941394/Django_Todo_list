import form as form
from django.shortcuts import render, redirect,HttpResponseRedirect
from django import forms
from .forms import addnot
from django.http import HttpResponse
from .models import add
# Create your views here.
def home(request):
    note = add.objects.all()
    if request.method == "POST":
        fm = addnot(request.POST)
        if fm.is_valid():

         fm.save()
    else:
     fm =  addnot()

    return render(request,'home.html',{'note':note})



def delete_data(request ,id):

        pi = add.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')



def update_data(request ,id):
    if request.method=="POST":
        pi = add.objects.get(pk=id)
        fm = addnot(request.POST,instance=pi)
        if fm.is_valid():
         pi.save()
    else:
        pi = add.objects.get(pk=id)
        fm = addnot(instance=pi)


    return render(request, 'edit.html' ,{'form':fm})



