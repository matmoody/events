from django.views.generic import TemplateView, View
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from calendar import monthcalendar
from datetime import datetime, date, timedelta
from .models import Event
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
import stripe
from django.urls import reverse
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

stripe.api_key = settings.STRIPE_SECRET_KEY

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

class HirePhotographerView(View):
    def get(self, request, event_id):
        event = get_object_or_404(Event, id=event_id)
        return render(request, 'partials/photographer_modal.html', {'event': event})

class RequestPhotographerView(View):
    def post(self, request, event_id):
        event = get_object_or_404(Event, id=event_id)
        
        # Get form data
        contact_name = request.POST.get('contact_name')
        contact_email = request.POST.get('contact_email')
        contact_phone = request.POST.get('contact_phone')
        notes = request.POST.get('notes')
        
        # # Send email
        # subject = f'Photographer Request for {event.title}'
        # message = render_to_string('emails/photographer_request.html', {
        #     'event': event,
        #     'contact_name': contact_name,
        #     'contact_email': contact_email,
        #     'contact_phone': contact_phone,
        #     'notes': notes,
        # })
        
        # send_mail(
        #     subject,
        #     message,
        #     settings.DEFAULT_FROM_EMAIL,
        #     [settings.PHOTOGRAPHER_EMAIL],  # Add this to your settings.py
        #     fail_silently=False,
        # )
        
        # Return success message
        return render(request, 'partials/photographer_modal.html', {
            'event': event,
            'success': True,
            'message': 'Your request has been sent! We will contact you shortly.'
        })

class CreateCheckoutSessionView(View):
    def get(self, request, event_id):
        event = get_object_or_404(Event, id=event_id)
        
        # Create Stripe checkout session
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'unit_amount': settings.PHOTOGRAPHER_PRICE,
                    'product_data': {
                        'name': f'Book A Photographer for {event.title} ',
                        'description': f'Professional photography coverage for this event on {event.event_date}. A photographer will attend the event, shoot a photo gallery, publish the photo gallery on Salina311, The Morning Briefing, and the Salina311 Newspaper. You will own the photos!',
                        'images': ['https://lrtest47.s3.us-east-1.amazonaws.com/gallery-example.png'],  # Optional
                    },
                },
                'quantity': 1,
            }],
            metadata={
                'event_id': event.id,
                'event_title': event.title,
                'event_date': event.event_date.isoformat(),
            },
            mode='payment',
            success_url=request.build_absolute_uri(
                reverse('checkout_success')
            ) + '?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=request.build_absolute_uri(reverse('home')),
        )
        
        return redirect(checkout_session.url)

class CheckoutSuccessView(View):
    def get(self, request):
        session_id = request.GET.get('session_id')
        if session_id:
            try:
                # Retrieve the full session data from Stripe
                session = stripe.checkout.Session.retrieve(session_id)
                #print(f"Session data: {session}")  # Debug print
                event = get_object_or_404(Event, id=int(session.metadata['event_id']))
                
                # Update event with photographer status
                event.photographer = True
                event.save()
                
                # Send confirmation emails
                send_booking_confirmation(event, session)
                
                return render(request, 'checkout_success.html', {'session': session})
                
            except Exception as e:
                print(f"Error processing checkout: {e}")
                # Handle error appropriately
                return render(request, 'checkout_success.html', {'error': str(e)})
                
        return render(request, 'checkout_success.html', {'error': 'Invalid session'})

def send_booking_confirmation(event, session):
    sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
    
    # Get customer email from session
    customer_email = session.customer_details.email
    #print(f"Customer email: {customer_email}")  # Debug print
    
    # Send email to customer
    html_content = render_to_string('emails/customer_photographer_booked.html', {
        'event': event,
        'session': session,
    })
    
    customer_message = Mail(
        from_email=('sarah@salina311.com', 'Salina311 Events'),
        to_emails=customer_email,
        subject=f'Salina311 Photographer Booking Confirmation: {event.title}',
        html_content=html_content
    )
    
    # Optional: Add categories or custom tracking settings
    # customer_message.category = ['photographer-booking']
    # print(f"Customer message: {customer_message}")
    
    try:
        sg.send(customer_message)
    except Exception as e:
        print(f"Error sending customer email: {e}")
