from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'key_features': [
                {'title': 'Event Coverage', 'description': 'Professional photography for all types of events in Salina.'},
                {'title': 'Full Galleries', 'description': 'Receive complete, high-resolution photo galleries of your event.'},
                {'title': 'Local Publication', 'description': 'Option to publish your photos on Salina311.com and local media.'},
                {'title': 'Custom Packages', 'description': 'Tailored photography packages to suit your event needs and budget.'},
            ],
            'how_it_works_steps': [
                {'description': 'Contact us to discuss your event details and photography needs.'},
                {'description': 'We will cover your event, capturing all the important moments.'},
                {'description': 'Receive your full photo gallery and choose your publication options.'},
            ],
            'benefits': [
                {'title': 'Local Expertise', 'description': 'We know Salina and its event scene inside out.', 'image': 'https://salina311.com/content/images/2024/08/Bishops-5.jpg'},
                {'title': 'Quality Photos', 'description': 'High-resolution, professionally edited images.', 'image': 'https://lrtest47.s3.amazonaws.com/event1.jpg'},
                {'title': 'Media Exposure', 'description': 'Get your event featured in local publications.', 'image': 'https://salina311.com/content/images/size/w2400/2024/10/SHHS10.11.24.jpg'},
                {'title': 'Hassle-Free', 'description': 'We handle everything, so you can focus on your event.', 'image': 'https://salina311.com/content/images/2024/10/_MG_2618.jpg'},
            ],
            'testimonials': [
                {
                    'name': 'Ashley McArthur',
                    'photo': 'https://salina311.com/content/images/2024/10/DSC_0134.jpg',
                    'quote': 'Long McArthur has used PhotographerSalina.com & Salina311 for photography at multiple Long McArthur events over the years. The whole experience is exceptional, they are great to work with and are very professional!',
                    'pain_point': 'Needed high-quality photos for events',
                    'solution': 'Provided professional event coverage and media publication',
                    'benefit': 'Increased attendance at subsequent events'
                },
                {
                    'name': 'Sally Hemmer',
                    'photo': 'https://salina311.com/content/images/size/w1000/2024/10/_MG_2750-1.jpg',
                    'quote': ' I recently asked PhotographerSalina.com if they could send a photographer to my son\’s tackle football game. I was really impressed with the professionalism of the photographer and the ease at which they got great shots without disturbing the players, coaches and game. They knew exactly what to capture and we ended up with amazing photos of our kids playing a sport they love. Thanks PhotographerSalina.com for supporting youth sports! ',
                    'pain_point': 'Wanted high quality photos of youth football games',
                    'solution': 'Event photography with local media publication',
                    'benefit': 'High quality photos and publicity for youth sports'
                },
            ],
            'faq_questions': [
                {'question': 'What types of events do you cover?', 'answer': 'We cover all types of events in Salina, including corporate gatherings, sports events, and community festivals.'},
                {'question': 'How does the local media publication work?', 'answer': 'We have partnerships with Salina311.com, the Salina311 Newspaper, and the Salina Morning Briefing email newsletter. You can choose to have your event photos featured in these local media outlets.'},
                {'question': 'How quickly will we receive our photos?', 'answer': 'If you choose to publish your photo gallery, it will appear on Salina311 within 24 hours, otherwise you\'ll receive your full photo gallery within 48 hours after your event.'},
                {'question': 'Do you offer videography services as well?', 'answer': 'Currently, we focus on photography, but we can recommend trusted local videographers if you need video coverage for your event.'},
            ],
            'hero_image': 'https://salina311.com/content/images/2024/10/25thAnn-13.jpg',
        })
        return context

class ServicesView(TemplateView):
    template_name = "services.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'services': [
                {
                    'title': 'Corporate Events',
                    'description': 'Professional photography for conferences, galas, award ceremonies, and team-building events.',
                    'image': 'https://salina311.com/content/images/2024/08/Bishops-16.jpg',
                    'features': ['On-site printing options', 'Branded photo backdrops', 'Executive portraits']
                },
                {
                    'title': 'Sports Events',
                    'description': 'Dynamic photography for local sports events, tournaments, and athletic competitions.',
                    'image': 'https://salina311.com/content/images/size/w1000/2024/10/SKK_5320.jpg',
                    'features': ['Action shots', 'Team photos', 'Event highlight reels']
                },
                {
                    'title': 'Community Festivals',
                    'description': 'Document the vibrant culture of Salina with our festival and community event coverage.',
                    'image': 'https://lrtest47.s3.amazonaws.com/event1.png',
                    'features': ['Crowd shots', 'Performer/artist portraits', 'Event timeline coverage']
                },
            ],
            'additional_services': [
                'Photo editing and retouching',
                'Rush delivery options',
                'Photo booth rentals',
                'Aerial photography (drone)',
                'Virtual event photography',
            ],
            'publication_options': [
                {'name': 'Salina311.com', 'description': 'Featured gallery on Salina\'s premier local news website'},
                {'name': 'Salina311 Newspaper', 'description': 'Print feature in the weekly Salina311 Newspaper'},
                {'name': 'Salina Morning Briefing', 'description': 'Highlight in the daily email newsletter'},
            ]
        })
        return context

class PortfolioView(TemplateView):
    template_name = "portfolio.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'portfolio_categories': [
                {
                    'name': 'Corporate Events',
                    'images': [
                        {'url': 'https://salina311.com/content/images/2024/05/gradey-30.jpg', 'alt': 'Public Event', 'caption': 'Meet & Greet'},
                        {'url': 'https://salina311.com/content/images/2024/04/longMc-24.jpg', 'alt': 'Chamber After Hours', 'caption': 'Chamber After Hours'},
                        {'url': 'https://salina311.com/content/images/2024/08/_B2A3779.jpg', 'alt': 'Ribbon Cutting', 'caption': 'Ribbon Cutting'},
                    ]
                },
                {
                    'name': 'Sports Events',
                    'images': [
                        {'url': 'https://salina311.com/content/images/2024/09/_MG_1700.jpg', 'alt': 'Marathon', 'caption': 'Salina Marathon'},
                        {'url': 'https://salina311.com/content/images/2024/04/baseball-47.jpg', 'alt': 'Baseball Game', 'caption': 'High School Baseball'},
                        {'url': 'https://salina311.com/content/images/2024/10/_MG_2618.jpg', 'alt': 'Youth Football', 'caption': 'Youth Football'},
                    ]
                },
                {
                    'name': 'Community Festivals',
                    'images': [
                        {'url': 'https://lrtest47.s3.amazonaws.com/event2.jpg', 'alt': 'Music Festival', 'caption': 'Salina Summer Music Fest'},
                        {'url': 'https://lrtest47.s3.amazonaws.com/event3.jpg', 'alt': 'Food Fair', 'caption': 'Annual Taste of Salina Food Fair'},
                        {'url': 'https://lrtest47.s3.amazonaws.com/event1.jpg', 'alt': 'Art Exhibition', 'caption': 'Downtown Art Walk'},
                    ]
                },
            ]
        })
        return context

class AboutView(TemplateView):
    template_name = "about.html"

class PricingView(TemplateView):
    template_name = "pricing.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'pricing_packages': [
                {
                    'name': 'Basic Event Coverage',
                    'price': '$599',
                    'features': [
                        'Up to 3 hours of coverage',
                        '100 edited digital photos',
                        'Online gallery for 30 days',
                        'Personal use rights',
                    ],
                    'best_for': 'Small gatherings and short events',
                },
                {
                    'name': 'Standard Event Package',
                    'price': '$999',
                    'features': [
                        'Up to 6 hours of coverage',
                        '250 edited digital photos',
                        'Online gallery for 60 days',
                        'Personal use rights',
                        '1 photographer + 1 assistant',
                        'Basic local media publication',
                    ],
                    'best_for': 'Medium-sized events',
                    'highlighted': True,
                },
                {
                    'name': 'Premium Event Coverage',
                    'price': '$1,499',
                    'features': [
                        'Up to 10 hours of coverage',
                        '500 edited digital photos',
                        'Online gallery for 90 days',
                        'Personal and commercial use rights',
                        '2 photographers',
                        'Comprehensive local media publication',
                        'Printed photo album',
                    ],
                    'best_for': 'Large events, festivals, and full-day coverage',
                },
            ],
            'additional_services': [
                {'name': 'Extra coverage time', 'price': '$150/hour'},
                {'name': 'Rush editing (48-hour turnaround)', 'price': '$250'},
                {'name': 'Additional photographer', 'price': '$350'},
                {'name': 'Photo booth rental', 'price': '$400'},
                {'name': 'Drone aerial photography', 'price': '$300'},
            ],
        })
        return context

class ContactView(TemplateView):
    template_name = "contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'typeform_url': 'https://your-typeform-url-here.typeform.com/to/XXXXXXXX',  # Replace with your actual Typeform URL
            'contact_info': {
                'email': 'sarah@photographersalina.com',
                'phone': '(785) 571-9640',
            }
        })
        return context

class BookingView(TemplateView):
    template_name = "booking.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'typeform_url': 'https://your-typeform-url-here.typeform.com/to/XXXXXXXX',  # Replace with your actual Typeform URL
            'booking_info': {
                'email': 'sarah@photographersalina.com',
                'phone': '(785) 571-9640',
            }
        })
        return context
