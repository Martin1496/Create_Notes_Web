"""
URL configuration for notes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Note.views import NoteCreateView, NoteUpdateView, NoteDeleteView, NoteShareView


urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('api/', include('notes.urls')),
    path('Note/create/', NoteCreateView.as_view(), name='note-create'),
    path('Note/<int:pk>/update/', NoteUpdateView.as_view(), name='note-update'),
    path('Note/<int:pk>/delete/', NoteDeleteView.as_view(), name='note-delete'),
    path('Note/<int:pk>/share/', NoteShareView.as_view(), name='note-share'),
]
