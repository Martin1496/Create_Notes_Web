from django.shortcuts import render
from Note.models import Note

def home(request):
    notes = Note.objects.filter(user=request.user)
    context = {
        'notes': notes,
    }
    return render(request, 'home.html', context)
