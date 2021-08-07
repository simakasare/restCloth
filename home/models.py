from django.db import models
class Category(models.Model):
    category_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.category_name

  
class Product(models.Model):
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/products')
    price = models.CharField(max_length=20)
    description = models.TextField()
    stock = models.IntegerField(default=100)

    def __str__(self):
        return self.product_name

    

# Create your models here.
