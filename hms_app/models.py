from django.db import models

class UserProfile(models.Model):
    id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=255)
    emailid = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    
class Items(models.Model):
    item_id = models.AutoField(primary_key=True)
    itemname = models.CharField(max_length=100)
    image = models.ImageField(upload_to='menuapp/images/')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.CharField(max_length=20)
    description = models.TextField()

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    itemname =  models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField()
    totalamount = models.DecimalField(max_digits=8, decimal_places=2)
    
    def calculate_profit(self):
        cost = self.price * self.quantity
        profit = self.totalamount - cost
        return profit

    
    

