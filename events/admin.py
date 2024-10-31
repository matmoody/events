from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_date', 'event_start_time', 'location', 'category', 'photographer')
    list_filter = ('event_date', 'location', 'category')
    search_fields = ('title', 'description', 'location')
