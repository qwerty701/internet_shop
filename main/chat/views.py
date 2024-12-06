from django.shortcuts import render

def room(request, room_name):
    return render(request, 'chat/chat.html', {
        'room_name': room_name
    })

def chat(request):
    return render(request, 'chat/chat.html')