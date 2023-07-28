from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    TEXT = 'text'
    AUDIO = 'audio'
    VIDEO = 'video'
    NOTE_TYPES = [
        (TEXT, 'Text'),
        (AUDIO, 'Audio'),
        (VIDEO, 'Video'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    note_type = models.CharField(max_length=5, choices=NOTE_TYPES, default=TEXT)
    content = models.TextField(blank=True)
    audio_file = models.FileField(upload_to='audio/', blank=True)
    video_file = models.FileField(upload_to='video/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class SharedNote(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    shared_with = models.ForeignKey(User, on_delete=models.CASCADE)
