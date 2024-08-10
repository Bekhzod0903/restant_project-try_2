from django.db import models

class Customer(models.Model):
    cust_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    contact = models.BigIntegerField()
    address = models.TextField()
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Crew(models.Model):
    crew_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    contact = models.BigIntegerField()
    address = models.TextField()
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Food(models.Model):
    food_id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='food_images/')
    name = models.CharField(max_length=30)
    status = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Menu(models.Model):
    menu_id = models.AutoField(primary_key=True)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    details = models.CharField(max_length=255)

    def __str__(self):
        return self.details

class OrderDetails(models.Model):
    order_id = models.AutoField(primary_key=True)
    crew = models.ForeignKey(Crew, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=255)

    def __str__(self):
        return f"Order {self.order_id} - {self.customer.name}"

class Delivery(models.Model):
    delivery_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(OrderDetails, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return f"Delivery {self.delivery_id} - Order {self.order.order_id}"

class Payment(models.Model):
    pay_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order = models.ForeignKey(OrderDetails, on_delete=models.CASCADE)
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f"Payment {self.pay_id} - Order {self.order.order_id}"

class Transaction(models.Model):
    trans_id = models.AutoField(primary_key=True)
    trans_date = models.DateField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    crew = models.ForeignKey(Crew, on_delete=models.CASCADE)
    order = models.ForeignKey(OrderDetails, on_delete=models.CASCADE)
    report_date = models.DateField()

    def __str__(self):
        return f"Transaction {self.trans_id} - Order {self.order.order_id}"
