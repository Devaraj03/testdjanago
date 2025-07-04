from django.shortcuts import render,redirect,get_object_or_404
from .models import comics
from .forms import *

def home(request):
    comic=comics.objects.all()
    return render(request,'frontend/index.html',{'comic':comic})

def create(request):
    form=ComicsForm(request.POST,request.FILES)
    if form.is_valid():
        form.save()
        return redirect('home')
    else:
        form = ComicsForm()
    return render(request,'frontend/createform.html',{'form':form})

def update(request,pk):
    comic=get_object_or_404(comics,pk=pk)
    form=ComicsForm(request.POST or None,request.FILES,instance=comic)
    if form.is_valid():
        form.save()
        return redirect('home')
    else:
        form = ComicsForm(instance=comic) 
    return render(request,'frontend/createform.html',{'form':form})

def delete(request,pk):
    form=get_object_or_404(comics,pk=pk)
    if request.method=="POST":
        form.delete()
        return redirect('home')
    return render(request,'frontend/delete.html',{'form':form})