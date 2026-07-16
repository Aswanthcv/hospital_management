from django import forms
from .models import *

class DateInput(forms.DateInput):
  input_type = 'date'

class BookingForm(forms.ModelForm):
  class Meta:
    model = Booking
    fields = '__all__'

    widgets = {
      'booking_date':DateInput(),
    }

    labels = {
      'p_name':"Name",
      'p_phone':"Phone",
      'p_email':"Email",
      'doc_name':"Doctor name",
      'booking_date':"Booking date"
    }