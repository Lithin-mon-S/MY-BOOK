from django.db.models import Q
from django.shortcuts import render, redirect
from .forms import AuthorForm, BookForm
# Create your views here.
from .models import Book
from django.core.paginator import Paginator, EmptyPage


# def creatbook(request):
#   books = Book.objects.all()

# if request.method=='POST':
#    title=request.POST.get('title')
#   price=request.POST.get('price')

# book=Book(title=title,price=price)

# book.save()
# return render(request, 'book.html',{'books':books})


def creatbook(request):
    books = Book.objects.all()

    if request.method == 'POST':
        form = BookForm(request.POST, files=request.FILES)

        if form.is_valid():
            form.save()

            return redirect('/')

    else:
        form = BookForm()

    return render(request, 'admin/book.html', {'form': form, 'books': books})


def Create_Author(request):
    if request.method == 'POST':

        form = AuthorForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/')

    else:
        form = AuthorForm()

    return render(request, 'admin/author.html', {'form': form})


def listBook(request):
    books = Book.objects.all()

    paginator = Paginator(books, 4)
    page_number = request.GET.get('page')

    try:
        page = paginator.get_page(page_number)

    except EmptyPage:
        page = paginator.page(page_number.num_pages)

    return render(request, 'admin/booklist.html', {'books': books, 'page': page})


def detailviews(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'admin/detailviews.html', {'book': book})


def updatebook(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)

        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = BookForm(instance=book)

    return render(request, 'admin/updatebook.html', {'form': form})


#  book = Book.objects.get(id=book_id)

# if request.method=='POST':
#    title=request.POST.get('title')
#   price=request.POST.get('price')


#  book.title=title
# book.price=price

# book.save()

# return redirect('/')

# return render(request,'updatebook.html',{'book':book})

def Deleteview(request, book_id):
    book = Book.objects.get(id=book_id)

    if request.method == 'POST':
        book.delete()
        return redirect('/')

    return render(request, 'admin/Deleteview.html', {'book': book})


def index(request):
    return render(request, 'admin/base.html')


def Search_Book(request):
    query = None
    books = None

    if 'q' in request.GET:

        query = request.GET.get('q')
        books = Book.objects.filter(Q(title__icontains=query) | Q(author__name__icontains=query))
    else:
        books = []

    context = {'books': books, 'query': query}
    return render(request, 'admin/search.html', context)
