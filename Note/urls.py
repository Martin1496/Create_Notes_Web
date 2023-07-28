from django.urls import path
from Note.views import NoteListCreateAPIView, NoteDetailAPIView, SharedNoteListAPIView

urlpatterns = [
    path('notes/', NoteListCreateAPIView.as_view(), name='note-list-create'),
    path('notes/<int:pk>/', NoteDetailAPIView.as_view(), name='note-detail'),
    path('shared-notes/', SharedNoteListAPIView.as_view(), name='shared-note-list'),
]
