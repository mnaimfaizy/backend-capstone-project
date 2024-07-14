from rest_framework.serializers import ModelSerializer

from .models import Booking, Menu

class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

class MenuSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'