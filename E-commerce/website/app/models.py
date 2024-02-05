from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.utils.text import slugify
    
class Tag(models.Model):
        tags_id = models.AutoField(primary_key=True)
        tags_name = models.CharField(max_length=100)

        def __str__(self):
            return self.tags_name
        
    
    
class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    sub_category_id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    
class Product(models.Model):
    product_title = models.CharField(max_length=255)
    product_description = models.TextField()
    product_base_price = models.IntegerField()
    product_discounted_price = models.IntegerField()
    in_stock = models.BooleanField(default=False)
    product_quantity = models.IntegerField()
    product_images = models.ImageField(upload_to="my_image")  
    product_tags = models.ManyToManyField(Tag, related_name='products')
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategory, related_name='products', on_delete=models.CASCADE)  # Add this line
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def __str__(self):
        return self.product_title
    
class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review_date =  models.DateTimeField(auto_now_add=True)
    review_text = models.TextField()
   

    def __str__(self):
        return f"Review {self.review_id} by {self.user}"

    
class Offer(models.Model):
    offer_id=models.AutoField(primary_key=True)
    offer_category=models.CharField(max_length=100)
    offer_description=models.TextField(max_length=500)
    
class Newsletter(models.Model):
    email=models.EmailField()


class ProductSubCategory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    
class CartItem(models.Model):
    user = models.IntegerField()
    product_id = models.IntegerField()
    quantity = models.IntegerField()
    
class Like(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Dislike(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='dislikes')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
class  SpecifiactionName(models.Model):
    name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    

class SpecifiactionValue(models.Model):
    product= models.ForeignKey(Product,on_delete=models.CASCADE)
    name=models.ForeignKey(SpecifiactionName,on_delete=models.CASCADE)
    value=models.CharField(max_length=100)


  


    

    
     
    
    