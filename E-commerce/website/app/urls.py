from django.contrib import admin
from django.urls import path,include
from app import views

urlpatterns = [
    path('product/',views.product_list),
    path('offer/',views.Offer_list),
    path('newsletter/',views.newsletter),#Post
    path('add_cart/',views.add_cart),#POST
    path('review/<slug:slug>',views.review_list),
    path('category/<slug:slug>',views.category),
    path('likes/',views.like_create),
    path('dislike/',views.dislike_create),
    path('category_list/',views.Category_list),
    path('get_subcategories/<int:category_id>',views.get_subcategories, name='get_subcategories'),
    path('related_products/<slug:slug>/',views.related_products),
    

    
]
