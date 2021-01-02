from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Item
from django.template import loader
from .forms import ItemForm
from django import forms
# Create your views here.
def index(request):
    item_name = Item.objects.all()
    context ={
                    'item_name':item_name
    }
    return render(request,'food/index.html',context)

def itom(request):
    return HttpResponse('<h1> This is  a item view </h1>')

def page1(request):
    return HttpResponse("<button> Hello </button>")

def detail(request,item_id):
    item = Item.objects.get(pk=item_id)
    context={
        'item':item,
    }
    return render(request,'food/details.html',context)

def add_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/food/')
    f = {
        'form':form
    }

    return render(request,'food/item-form.html',f)

def edit_item(request,id_item):
    item =Item.objects.get(id=id_item)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('/food/')
    return render(request,'food/item-form.html',{'form':form,'item':item})

def delete_item(request,id):
    item = Item.objects.get(id=id)
    if request.method == 'POST':
        item.delete()
        return redirect('/food/')

    return render(request,'food/delete_item.html',{'item':item})

def delete_base(request):
    return render(request,'food/delete_temp.html')
