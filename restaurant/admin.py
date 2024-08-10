from django.contrib import admin
from .models import Customer, Crew, Food, Menu, OrderDetails, Delivery, Payment, Transaction

admin.site.register(Customer)
admin.site.register(Crew)
admin.site.register(Food)
admin.site.register(Menu)
admin.site.register(OrderDetails)
admin.site.register(Delivery)
admin.site.register(Payment)
admin.site.register(Transaction)
