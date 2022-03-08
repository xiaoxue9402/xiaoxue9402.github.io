from django.shortcuts import render
from . import sample_epubs
from .models import Book


def index(request):
    return render(request,'index.html', {
        'book': Book.objects.all()
    })
