from django.views.generic import TemplateView, View
from django.shortcuts import render
from django.utils import timezone
from calendar import monthcalendar
from datetime import datetime, date, timedelta
from .models import Event


class CalendarView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Get current date info
        today = timezone.localtime().date()
        year = int(self.request.GET.get('year', today.year))
        month = int(self.request.GET.get('month', today.month))
        
        # Calculate previous and next months
        if month == 1:
            prev_month, prev_year = 12, year - 1
        else:
            prev_month, prev_year = month - 1, year
            
        if month == 12:
            next_month, next_year = 1, year + 1
        else:
            next_month, next_year = month + 1, year
        
        # Get all events for the month
        month_start = date(year, month, 1)
        month_end = date(year + 1, 1, 1) if month == 12 else date(year, month + 1, 1)
        
        events = Event.objects.filter(
            event_date__gte=month_start,
            event_date__lt=month_end
        ).order_by('event_date', 'event_start_time')
        
        # Get today's events
        todays_events = Event.objects.filter(
            event_date=today
        ).order_by('event_start_time')
        
        # Build calendar data
        calendar_data = []
        for week in monthcalendar(year, month):
            week_data = []
            for day in week:
                if day == 0:
                    week_data.append((None, []))
                else:
                    current_date = date(year, month, day)
                    day_events = [e for e in events if e.event_date == current_date]
                    week_data.append((current_date, day_events))
            calendar_data.append(week_data)
        
        # Add mobile view data
        days_data = self.get_days_data(today, days_ahead=7)
        
        # Update context
        context.update({
            'calendar_data': calendar_data,
            'month_name': month_start.strftime('%B'),
            'year': year,
            'today': today,
            'current_month': month,
            'prev_month': prev_month,
            'prev_year': prev_year,
            'next_month': next_month,
            'next_year': next_year,
            'todays_events': todays_events,
            'days_data': days_data,
            'last_date': today + timedelta(days=7),
        })
        
        return context
    
    def get_days_data(self, start_date, days_ahead=7):
        days_data = []
        for i in range(days_ahead):
            current_date = start_date + timedelta(days=i)
            events = Event.objects.filter(
                event_date=current_date
            ).order_by('event_start_time')
            
            days_data.append({
                'date': current_date,
                'events': events,
            })
        return days_data

class EventsForDateView(View):
    def get(self, request):
        # Get current date info
        today = timezone.localtime().date()
        
        # Get selected date from request
        selected_date_str = request.GET.get('date')
        try:
            selected_date = datetime.strptime(selected_date_str, '%Y-%m-%d').date()
        except (ValueError, TypeError):
            selected_date = today
        
        # Get selected day's events
        selected_events = Event.objects.filter(
            event_date=selected_date
        ).order_by('event_start_time')
        
        context = {
            'selected_date': selected_date,
            'selected_events': selected_events,
            'today': today,
        }
        
        return render(request, 'partials/events_sidebar.html', context)

class LoadMoreDaysView(View):
    def get(self, request):
        last_date_str = request.GET.get('last_date')
        try:
            last_date = datetime.strptime(last_date_str, '%Y-%m-%d').date()
        except (ValueError, TypeError):
            last_date = timezone.localtime().date()
        
        start_date = last_date + timedelta(days=1)
        days_data = self.get_days_data(start_date, days_ahead=7)
        
        context = {
            'days_data': days_data,
            'last_date': start_date + timedelta(days=7),
            'today': timezone.localtime().date(),
        }
        
        return render(request, 'partials/mobile_events_list.html', context)
    
    def get_days_data(self, start_date, days_ahead=7):
        # Same as CalendarView.get_days_data
        days_data = []
        for i in range(days_ahead):
            current_date = start_date + timedelta(days=i)
            events = Event.objects.filter(
                event_date=current_date
            ).order_by('event_start_time')
            
            days_data.append({
                'date': current_date,
                'events': events,
            })
        return days_data
