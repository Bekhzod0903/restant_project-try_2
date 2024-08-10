from django.urls import path
from .views import (
    landing_page,
    create_customer,
    customer_list,
    create_crew,
    crew_list,
    create_food,
    food_list,
    create_order,
    order_list,
    create_payment,
    payment_list,
    create_transaction,
    transaction_list,
)

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('customers/new/', create_customer, name='create_customer'),
    path('customers/', customer_list, name='customer_list'),
    path('crew/new/', create_crew, name='create_crew'),
    path('crew/', crew_list, name='crew_list'),
    path('food/new/', create_food, name='create_food'),
    path('food/', food_list, name='food_list'),
    path('orders/new/', create_order, name='create_order'),
    path('orders/', order_list, name='order_list'),
    path('payments/new/', create_payment, name='create_payment'),
    path('payments/', payment_list, name='payment_list'),
    path('transactions/new/', create_transaction, name='create_transaction'),
    path('transactions/', transaction_list, name='transaction_list'),
]
