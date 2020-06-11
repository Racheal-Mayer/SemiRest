from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

def index(request):
    context = {
        "show" : Show.objects.all()
    }
    return render(request, "index.html", context)

def addshow(request):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        Show.objects.create(title=request.POST['title'],
        desc= request.POST['desc'], 
        date = request.POST['date'], 
        network = request.POST['network'])
        messages.success(request, "Show successfully Entered!")
    return redirect("/")

def edit(request,show_id):
    context = {
        "show_id" : show_id
    }
    return render(request, "edit.html", context)

def process_edit(request, show_id):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/edit/{show_id}')
    else:
    # use id to grab show
        show_to_edit = Show.objects.get(id=show_id)
        # edit the value field with post date
        show_to_edit.title = request.POST['title']
        show_to_edit.date = request.POST['date']
        show_to_edit.network = request.POST['network']
        show_to_edit.desc = request.POST['desc']
        # save the show
        show_to_edit.save()
        messages.success(request, "Show successfully Entered!")
        return redirect('/')

def delete(request, show_id):
    show_to_delete = Show.objects.get(id=show_id)
    show_to_delete.delete()
    return redirect('/')

def show (request, show_id):
    context = {
        "show" : Show.objects.get(id=show_id)
    }
    return render(request, "show.html", context)