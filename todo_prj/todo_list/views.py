from django.shortcuts import render, redirect
from .models import list
from .forms import Listform
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

def home( request ):

    if request.method == 'POST':
        form = Listform(request.POST or None)

        if form.is_valid():
            form.save()
        all_items = list.objects.all
        messages.success(request, ('Item has been added to the list!'))
        return render(request, 'home.html', {'all_items': all_items})
    else:
        all_items = list.objects.all
        return render(request, 'home.html', {'all_items': all_items})

def delete(request, list_id):
        item = list.objects.get(pk=list_id)
        item.delete()
        messages.success(request, ('Item has been deleted!'))
        return redirect('home')

def cross_off(request, list_id):
        item = list.objects.get(pk=list_id)
        item.completed = True
        item.save()
        all_items = list.objects.all
        return redirect('home')


def uncross(request, list_id):
    item = list.objects.get(pk=list_id)
    item.completed = False
    item.save()
    all_items = list.objects.all
    return redirect('home')


def edit(request, list_id ):

    if request.method == 'POST':
        item = list.objects.get(pk=list_id)


        form = Listform(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            messages.success(request, ('Item has been updated!'))
            return redirect('home')

    else:
        item = list.objects.get(pk=list_id)
        return render(request, 'edit.html', {'item': item})

def SingUp(request):
    return render(request, 'authenticate/SignUp.html',{})


