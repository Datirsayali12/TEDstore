from rest_framework import serializers
from .models import Product,Offer,Newsletter,Category,SubCategory,Review,CartItem,Like,Dislike

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'
        
class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model=Offer
        fields='__all__'
        
class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Newsletter
        fields='__all__'
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'
        
class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=SubCategory
        fields='__all__'
        
# class ProductSpecificationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=ProductSpecification
#         fields='__all__'
        
class ReviewSerializer(serializers.ModelSerializer):
    total_likes = serializers.SerializerMethodField()
    
    class Meta:
        model = Review
        fields = '__all__'

    def get_total_likes(self, obj):
        return obj.likes.count()


        
class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=CartItem
        fields='__all__'
        
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'

class DislikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dislike
        fields = '__all__'
        
# class ProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Profile
#         fields = '__all__'
        

        
        