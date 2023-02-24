from django.shortcuts import render, redirect
from .models import Classes
from django.contrib import messages
# Create your views here.

def home(request):
    class_list = Classes.objects.all()
    messages.success(request, 'Classes Listed')
    return render(request, "managementClass.html",{ "classes": class_list})

def addClass(request):
    code = request.POST["txtCode"]
    name = request.POST["txtName"]
    credits = request.POST["numCredits"]

    Course = Classes.objects.create(code = code, name = name, credits = credits)
    messages.success(request, 'Class Added')
    return redirect('/')

def deleteClass(request, code):
    Course = Classes.objects.get(code = code)
    Course.delete()
    messages.success(request, 'Class Deleted')
    return redirect('/')

def editionClass(request, code):
    Course = Classes.objects.get(code = code)
    return render(request, "editionClass.html", {"class": Course})

def editClass(request):
    code = request.POST["txtCode"]
    name = request.POST["txtName"]
    credits = request.POST["numCredits"]

    Course = Classes.objects.get(code = code)
    Course.name = name
    Course.credits = credits
    Course.save()

    messages.success(request, 'Class Updated')

    return redirect('/')
    
