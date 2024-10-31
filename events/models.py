from django.db import models

# Create your models here.

class Event(models.Model):
    CATEGORY_CHOICES = [
        ('ENTERTAINMENT', 'Entertainment'),
        ('SPORTS', 'Sports'),
        ('ARTS', 'Arts'),
        ('GOVERNMENT', 'Government'),
        ('OTHER', 'Other'),
    ]
    
    title = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    event_date = models.DateField(auto_now=False, null=True, blank=True, verbose_name="Start Date")
    event_start_time = models.TimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    photographer = models.BooleanField(default=False)
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='OTHER'
    )
    
    class Meta:
        ordering = ['event_date']
    
    def __str__(self):
        return self.title

