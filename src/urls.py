"""
URL configuration for src project.

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
from django.urls import path
from events.views import CalendarView, EventsForDateView, LoadMoreDaysView, HirePhotographerView, RequestPhotographerView, CreateCheckoutSessionView, CheckoutSuccessView

urlpatterns = [
    path('', CalendarView.as_view(), name='home'),
    path('events-for-date/', EventsForDateView.as_view(), name='events_for_date'),
    path('load-more-days/', LoadMoreDaysView.as_view(), name='load_more_days'),
    path('admin/adshp98q3gwpf9uerphieagouqefy8dtuyfydrdr', admin.site.urls),
    path('hire-photographer/<int:event_id>/', HirePhotographerView.as_view(), name='hire_photographer'),
    path('request-photographer/<int:event_id>/', RequestPhotographerView.as_view(), name='request_photographer'),
    path('create-checkout-session/<int:event_id>/', 
         CreateCheckoutSessionView.as_view(), 
         name='create_checkout_session'),
    path('checkout-success/', 
         CheckoutSuccessView.as_view(), 
         name='checkout_success'),
]