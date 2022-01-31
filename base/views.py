from django.shortcuts import render
from django.http import HttpResponse

rooms = [
    {'id': 1, 'name': 'Lets learn python!'},
    {'id': 2, 'name': 'Design with me'},
    {'id': 3, 'name': 'Frontend Developers'},
]
name = 'Gaurav Anthwal'

# Create your views here.
def home(request):
    context = {'rooms': rooms, 'name': name}
    return render(request, 'base/home.html', context)

def rooms(request):
    return render(request, 'base/rooms.html', )

def room(request, pk):
    return render(request, 'base/room.html', {'pk': pk})

