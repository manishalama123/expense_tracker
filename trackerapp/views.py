from django.shortcuts import render,redirect,get_object_or_404
from .forms import TrackerForm
from .models import Tracker

def index(request):
    expenses=Tracker.objects.all()
    return render(request,'index.html',{'expenses':expenses})


# Create your views here.
def add(request):
    if request.method=='POST':
        form= TrackerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form=TrackerForm()
    
    return render(request,'add.html',{'form':form})

def update(request,id):
    expense=get_object_or_404(Tracker,id=id)
    if request.method=='POST':
        form=TrackerForm(request.POST, request.FILES, instance=expense)
        if form.is_valid:
            form.save()
            return redirect('index')
    else:
        form=TrackerForm(instance=expense)
    return render(request,'update.html',{'form':form})

def delete(request,id):

        expense=get_object_or_404(Tracker,id=id)
        expense.delete()
        return redirect('index')


