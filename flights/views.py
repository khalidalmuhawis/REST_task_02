from rest_framework.generics import ListAPIView
from datetime import datetime
from .models import Flight, Booking
from .serializers import FlightSerializer, BookingSerializer, BookingDetailSerializer, BookingCreateSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView
class FlightsList(ListAPIView):
	queryset = Flight.objects.all()
	serializer_class = FlightSerializer


class BookingsList(ListAPIView):
	queryset = Booking.objects.filter(date__gte=datetime.today())
	serializer_class = BookingSerializer

class BookingUpdateView(RetrieveUpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class =  BookingCreateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'booking_id'

class BookingDetailView(RetrieveAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'booking_id'

class BookingDeleteView(DestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class =  BookingCreateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'booking_id'
