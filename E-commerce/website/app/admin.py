from django.contrib import admin
from .models import Product,Offer,Newsletter,Category,SubCategory,Tag,Review,CartItem,Like,Dislike,SpecifiactionName,SpecifiactionValue,ProductSubCategory
from django.contrib.auth.admin import UserAdmin
admin.site.register(Product)

    
@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display=['offer_id','offer_category','offer_description']
    
@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display=['email']
    


admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Review)
admin.site.register(ProductSubCategory)

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display=['user','product_id','quantity']
    
@admin.register(Like)
class LikeemAdmin(admin.ModelAdmin):
    list_display=['user_id','review_id']
    
@admin.register(Dislike)
class DislikeItemAdmin(admin.ModelAdmin):
    list_display=['user_id','review_id']
    

@admin.register(SpecifiactionValue)
class SpecificationValueAdmin(admin.ModelAdmin):
    list_display=['name','value']


@admin.register(SpecifiactionName)
class SpecificationNameAdmin(admin.ModelAdmin):
    list_display=['name']






