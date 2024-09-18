from django.shortcuts import render,redirect
from .models import Book
from .forms import BookForm
# Create your views here.


def book_list(request):
    books=Book.objects.all()
    return render(request,'crud/index.html',{'books':books})

def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'crud/form.html', {'form': form})

# def Form(request):
#     form=BookForm()
#     return render(request,'crud/form.html',{'form':form})

# def index(request):
#     return render(request,'crud/index.html')

# def create_book(request):
#     form=BookForm(request.POST)
#     if form.is_valid():
#         form.save()
#         return redirect('book_list')
#     return redirect('book_list')



def delete_book(request,id):
    book=Book.objects.get(pk=id)
    book.delete()
    return redirect('book_list')


# def update_book(request,id):
#     book=Book.objects.get(pk=id)  
#     book.name='My name is Talha'
#     book.save()
#     return redirect('book_list')