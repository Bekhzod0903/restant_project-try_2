from django import forms
from .models import Customer, Crew, Food, OrderDetails, Payment, Transaction

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'contact', 'address', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

class CrewForm(forms.ModelForm):
    class Meta:
        model = Crew
        fields = ['name', 'contact', 'address', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['name', 'status', 'price']

class OrderDetailsForm(forms.ModelForm):
    class Meta:
        model = OrderDetails
        fields = ['crew', 'customer', 'food', 'date', 'status']

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['customer', 'order', 'amount', 'date']

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['customer', 'crew', 'order', 'trans_date', 'report_date']
