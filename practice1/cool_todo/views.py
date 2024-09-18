from django.shortcuts import render,HttpResponse,redirect
from  .forms import TodoForm
from .models import Todo


def todos(request):
    if request.method=='POST':
        form=TodoForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('home_page')
    
    data=Todo.objects.all()
    form=TodoForm()
    return render(request,'index.html',{
        'data':data,
        'form':form
    })
    
        
    