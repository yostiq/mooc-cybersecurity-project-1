from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Note
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
import sqlite3

@login_required
def index(request):
    user_notes = Note.objects.filter(owner_id=request.user.id)
    public_notes = Note.objects.filter(private = False).exclude(owner_id=request.user.id)
    return render(request, 'notes/index.html', { 'user_notes' : user_notes, 'public_notes' : public_notes })

@login_required
@csrf_exempt
def addnote(request):
    note = Note()
    note.note_text = request.POST['note_text']
    note.pub_date = timezone.now()
    note.owner = request.user
    try:
        if request.POST['public_note'] == 'on':
            note.private = False
    except:
        note.private = True
    note.save()

    notes = Note.objects.filter(owner_id=request.user.id)
    return redirect('/')

def readnote(request, noteid):
     note = Note.objects.get(pk=noteid)
     response = HttpResponse(note.note_text, content_type='text/html')
     return response

## Flaws 1, 3 and 5 are fixed by replacing the other readnote function with this one
# @login_required
# def readnote(request, noteid):
#     note = Note.objects.get(pk=noteid)
#     if request.user == note.owner:
#         response = HttpResponse(note.note_text, content_type='text/plain')
#         return response
#     else:
#         return render(request, 'notes/forbidden.html')

def deletenote(request):
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    note_to_delete = request.POST['note_text']
    try:
        response = cursor.execute('DELETE FROM notes_note WHERE note_text=\'' + note_to_delete + '\';')
        conn.commit()
    except:
        pass
    return redirect('/')

## Flaw 4 fixed with this function
# @login_required
# def deletenote(request):
#     note_to_delete = request.POST['note_text']
#     Note.objects.filter(note_text = note_to_delete, owner = request.user).delete()
#     return redirect('/')
