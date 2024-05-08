from random import randint

from django.http import HttpResponse
from django.shortcuts import render, redirect

from biblioteczka.models import Author, Publisher, Book, Genre
from biblioteczka.moje_zabawki import lst, Car
from start_pyt18.ksiazki import lst2, Books


# Create your views here.


# def index(request):
#     return HttpResponse("""
#     <ul>
#     <li><a href="/">pierwsza</a></li>
#     <li><a href="/index2/">druga</a></li>
#     <li><a href="/next/">trzecia</a></li>
#     moja stronka heh
#     """)

def index(request):
    return render(request, 'index.html')


def index2(request):
    return render(request, 'index2.html')

def dodawanie(request, a, b):
    return HttpResponse(f'{a} + {b} = {a+b}')

def odejmowanie(request, a, b):
    return HttpResponse(f"""
    ODEJMOWANIE <br>
    {a} - {b} = {a-b}<br>
    MNOZENIE<br>
    {a} * {b} = {a*b}
    
    """)

def mnozenie(request, a, b):
    return HttpResponse(f'{a} * {b} = {a*b}')

def dzielenie(request, a, b):
    if a == 0 or b == 0:
        return HttpResponse('nie dziel przez zerooooo')
    else:
        return HttpResponse(f'{a} / {b} = {a/b}')


def tabliczka(request, a, b):

    result = "<table border ='1'>"
    for i in range(1, a+1):
        result += '<tr>'
        for j in range(1, b+1):
            result += f'<td>{i * j}</td>'
        result += "</tr>"
    result += "<table>"
    return HttpResponse(f'tabliczka {a} x {b}', result)


def losuj(request):
    liczba = randint(1, 100)
    return render(request, 'liczba.html', {'zz': liczba})




def losuj2(request, a, b, ilosc):
    liczby = []
    for i in range(ilosc):
        liczby.append(randint(a, b))
    return render(request, 'liczba.html', {'zz': liczby})


def next(request):
    return render(request, 'index3.html')


def cars(request):
    CARS = lst
    return render(request, 'samochody.html', {'cars': CARS})


def mycar(request, a):
    try:
        mycar = lst[a]
    except IndexError:
        return HttpResponse("brak")
    return render(request, 'samochody.html', {'cars': [mycar]})


def books2(request):
    BOOKS = lst2
    return render(request, 'ksiazki.html', {'books': BOOKS})


def add_car(request):
    if request.method == 'POST':
        model = request.POST['model']
        marka = request.POST['marka']
        c = Car(model=model, marka=marka)
        lst.append(c)
    return render(request, 'add_car.html')


def add_book1(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        year = request.POST['year']
        b = Books(title=title, author=author, year=year)
        lst2.append(b)
    return render(request, 'add_book.html')


def del_car(request, index):
    car = lst.pop(index)
    return HttpResponse(f'usunalem {car}')


def add_author(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        a = Author.objects.create(first_name=first_name, last_name=last_name)

    return render(request, 'add_author.html')


def authors_list(request):
    authors = Author.objects.all()
    imie = request.GET.get('first_name', "")  ## dzieki temu ze GEt.get, program nam sie nie wysypie jesli nie podamy imienia w parametrze
    authors = authors.filter(first_name__icontains=imie)
    last_name = request.GET.get('last_name', "")
    authors = authors.filter(last_name__icontains=last_name)
    return render(request, 'authors.html', {'authors': authors})


# slawki = authors.filter(first_name='slawek')
# slawki = Author.objects.filter(first_name='slawek')
# authors = Author.objects.filter(id__gte=6)


# def delete_author(request, author_id):
#     if request.method == 'POST':
#         author = Author.objects.get(pk=author_id)
#         author.delete()
#         return


def delete_author(request, pk):
    author = Author.objects.get(id=pk)
    if request.method == "GET":
        return render(request, 'delete.html', {'author': author})
    else:
        action = request.POST['action']
        if action == 'YES':
            author.delete()
        return redirect('authors_list')

def add_publisher(request):
    if request.method == 'POST':
        name = request.POST['name']
        sub_name = request.POST['sub_name']
        Publisher.objects.create(name=name, sub_name=sub_name)
    return render(request, 'add_publisher.html')


def publishers_list(request):
    publishers = Publisher.objects.all()
    name = request.GET.get('name', "")
    publishers = publishers.filter(name__icontains=name)
    sub_name = request.GET.get('sub_name', "")
    publishers = publishers.filter(sub_name__icontains=sub_name)
    return render(request, 'publishers.html', {'publishers': publishers})


def book_list(request):
    books = Book.objects.all()
    return render(request, 'books.html', {'books': books})


# def mypublisher(request, a):
#     try:
#         mypublisher = publishers[a]
#     except IndexError:
#         return HttpResponse("brak")
#     return render(request, 'publishers.html', {'publishers': [mypublisher]})


def add_book(request):
    authors = Author.objects.all()
    genres = Genre.objects.all()
    if request.method == 'POST':
        title = request.POST.get('title')
        year = request.POST.get('year')
        author = request.POST.get('author')
        genres = request.POST.getlist('genre')
        b = Book.objects.create(title=title, year=year, author_id=author)
        b.genres.set(genres)
        return redirect('book_list')
    return render(request, 'add_book.html', {'authors': authors, 'genres': genres})


def detail_author(request, pk):
    author = Author.objects.get(id=pk)
    return render(request, 'detail_author.html', {'author': author})


def add_genre(request):
    genres = Genre.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        Genre.objects.create(name=name)
    return render(request, 'add_genre.html', {'genres': genres})


def genre_list(request):
        genres = Genre.objects.all()
        return render(request, 'genre.html', {'genres': genres})








