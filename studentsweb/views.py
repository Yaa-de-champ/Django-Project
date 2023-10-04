from django.shortcuts import render, redirect
from .models import Room
# from django.http import HttpResponse
from .forms import RoomForm


# Create your views here.

# def home(request):
#     return HttpResponse('Home Page')

# def room(request):
#     return HttpResponse("Room")


# rooms = [
#     {'id':1, 'name':"Let's learn python"},
#     {'id':2, 'name':"Design with me"},
#     {'id':3, 'name':"Software Engineer"},
# ]

def home(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request, 'studentsweb/home.html', context)

# def room(request, pk):
#     room = None
#     for i in rooms:
#         if i['id'] == int(pk):
#             room = i
#         context = {'room': room}
#     return render(request, 'studentsweb/room.html', context)


def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'studentsweb/room.html', context)


def createRoom(request):
    form = RoomForm()
    # if request.method == 'POST':
    #     print(request.POST)
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')


    context = {'form' : form}

    return render(request, 'studentsweb/room_form.html', context)

def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context={'form' : form}
    return render(request, 'studentsweb/room_form.html', context)