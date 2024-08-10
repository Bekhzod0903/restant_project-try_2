from django.shortcuts import render, redirect
from .forms import CustomerForm, CrewForm, FoodForm, OrderDetailsForm, PaymentForm, TransactionForm
from .models import Customer, Crew, Food, OrderDetails, Payment, Transaction


def landing_page(request):
    return render(request, 'landing_page.html')


def create_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'customer_form.html', {'form': form})

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer_list.html', {'customers': customers})

def create_crew(request):
    if request.method == 'POST':
        form = CrewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crew_list')
    else:
        form = CrewForm()
    return render(request, 'crew_form.html', {'form': form})

def crew_list(request):
    crew_members = Crew.objects.all()
    return render(request, 'crew_list.html', {'crew_members': crew_members})

def create_food(request):
    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('food_list')
    else:
        form = FoodForm()
    return render(request, 'food_form.html', {'form': form})

def food_list(request):
    foods = Food.objects.all()
    return render(request, 'food_list.html', {'foods': foods})

def create_order(request):
    if request.method == 'POST':
        form = OrderDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderDetailsForm()
    return render(request, 'order_form.html', {'form': form})

def order_list(request):
    orders = OrderDetails.objects.all()
    return render(request, 'order_list.html', {'orders': orders})

def create_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payment_list')
    else:
        form = PaymentForm()
    return render(request, 'payment_form.html', {'form': form})

def payment_list(request):
    payments = Payment.objects.all()
    return render(request, 'payment_list.html', {'payments': payments})

def create_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm()
    return render(request, 'transaction_form.html', {'form': form})

def transaction_list(request):
    transactions = Transaction.objects.all()
    return render(request, 'transaction_list.html', {'transactions': transactions})
