from django.contrib import admin
from notes_app.models import Note

# Register your models here.
class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')

admin.site.register(Note, NoteAdmin)