from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    fullname = models.CharField(max_length=50)
    phon_number = models.CharField(max_length=50) 
    
    
class Category(models.Model):
    name = models.CharField(max_length=50)
    
class Product(models.Model):
    name = models.CharField(max_length=50)
    categori_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    categori_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    guantiti = models.IntegerField()
    price = models.IntegerField()
    categori_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    
class Cart(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    cr_at = models.DateTimeField(auto_now_add=True)
    
class Cart_item(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    
    
    
class Order(models.Model):
    STATUS_CHOICES = [
        ("pending", "Ожидает обработки"),
        ("processing", "Обрабатывается"),
        ("shipped", "Отправлен"),
        ("completed", "Завершён"),
        ("cancelled", "Отменён"),
    ]

    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    status = models.CharField( max_length=20, choices=STATUS_CHOICES, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)

   
class OrderItem(models.Model):
    order = models.ForeignKey( Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product,on_delete=models.PROTECT)
    quantity = models.IntegerField()
    price = models.IntegerField()

    