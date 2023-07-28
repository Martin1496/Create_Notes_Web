from rest_framework import generics, permissions
from Note.models import Note, SharedNote
from Note.serializers import NoteSerializer, SharedNoteSerializer

class NoteListCreateAPIView(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class NoteDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

class SharedNoteListAPIView(generics.ListAPIView):
    queryset = SharedNote.objects.all()
    serializer_class = SharedNoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(shared_with=self.request.user)
