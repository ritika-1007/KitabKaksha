from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
	DIVISION_CHOICES = (
		('Prayagraj', 'Prayagraj'),
		('Lucknow', 'Lucknow'),
		('Kanpur', 'Kanpur'),
		('Varanasi', 'Varanasi'),
		('Agra', 'Agra'),
	)

	DISCRICT_CHOICES = (
		('Prayagraj', 'Prayagraj'),
		('Lucknow', 'Lucknow'),
		('Kanpur', 'Kanpur'),
		('Varanasi', 'Varanasi'),
		('Agra', 'Agra'),
	)

	PAYMENT_METHOD_CHOICES = (
		('Paytm', 'Paytm'),
		('PhonePe','PhonePe'),
		('Cash On Delivery','Cash On Delivery'),
	)

	division = forms.ChoiceField(choices=DIVISION_CHOICES)
	district =  forms.ChoiceField(choices=DISCRICT_CHOICES)
	payment_method = forms.ChoiceField(choices=PAYMENT_METHOD_CHOICES, widget=forms.RadioSelect())

	class Meta:
		model = Order
		fields = ['name', 'email', 'phone', 'address', 'division', 'district', 'zip_code', 'payment_method', 'account_no', 'transaction_id']
