from django.shortcuts import render
from . import sample_epubs


books = [sample_epubs]
def index(request):
    return render(request,'index', {
        'book': books
    })
