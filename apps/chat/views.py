from django.shortcuts import render, HttpResponse
from .models import Message, Room
from django.views.generic.detail import DetailView


# Create your views here.

def home(request):
    rooms = Room.objects.all()
    return render(request, 'chat/home.html', {
        'rooms': rooms,
        })

class RoomDetailView(DetailView):
    model = Room
    template_name = 'chat/list-messages.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
