from django.shortcuts import render,redirect
from .forms import BookForms,SearchForm,ModelBookForms
from .models import Book
from django.contrib import messages
# Create your views here.

def form_view(request):
    msg=""
    if request.method=='POST':
        form=BookForms(request.POST)
        if form.is_valid():
           # book=Book(
           #     name=form.cleaned_data.get('name'),
           #     purchase_date=form.cleaned_data.get('pur_data'),
           #     genre=form.cleaned_data.get('genre'),
           #     author=form.cleaned_data.get('author')
           # )
            book=Book.objects.create(
                name=form.cleaned_data.get('name'),
                purchase_date=form.cleaned_data.get('pur_data'),
                # genre=form.cleaned_data.get('genre'),
                book_author=form.cleaned_data.get('author')
            )
            book.save()
            msg='Book Added Sucessfully!!'
        else:
            msg=form.error
    else:
        form=BookForms()
    return render(request,'forms.html',{'msg':msg,'forms':form})



def booksearch(request):
    if request.method=='POST':
        form=SearchForm(request.POST)
        if form.is_valid():
            q=form.cleaned_data_get('q')
            book=Book.objects.filter(name__contains=q)
            form=None
            return render(request,'showtables.html',{'book':book,'form':SearchForm()})

    else:
        form=SearchForm()
        book=Book.objects.all()
    return render(request,'showtables.html',{'book':book,'forms':form})
    

def deletebook(request,id):
    book=Book.objects.get(id=id)
    book.delete()
    messages.success(request,'Deleted #'+str(id)+ 'successfully!!!')
    return redirect('/')

def editbook(request,id):
    book=Book.objects.filter(id=id)
    # book = get_object_or_404(Book, id=id)
    if request.method =='POST':
        form=ModelBookForms(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Book updated successfully')
            return redirect('/')
    else:
        form = ModelBookForms(instance=Book)
    return render(request,'editbook.html',{'form':form})

    