from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Note
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


@login_required
def index(request):
    user_notes = Note.objects.filter(owner_id=request.user.id)
    public_notes = Note.objects.filter(private = False).exclude(owner_id=request.user.id)
    return render(request, 'polls/index.html', { 'user_notes' : user_notes, 'public_notes' : public_notes })

@login_required
@csrf_exempt
def addnote(request):
    note = Note()
    note.note_text = request.POST['note_text']
    note.pub_date = timezone.now()
    note.owner_id = request.user
    try:
        if request.POST['public_note'] == 'on':
            note.private = False
    except:
        note.private = True
    note.save()

    notes = Note.objects.filter(owner_id=request.user.id)
    return redirect('/')