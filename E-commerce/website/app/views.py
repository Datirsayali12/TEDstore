from django.shortcuts import render,redirect
from .serializers import ProductSerializer,OfferSerializer,NewsletterSerializer,CategorySerializer,SubCategorySerializer,ReviewSerializer,CartItemSerializer,LikeSerializer,DislikeSerializer
from .models import Product,Offer,Category,SubCategory,Review
from rest_framework.renderers import JSONRenderer
import io
from django.http import HttpResponse,JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.contrib.auth.models import User,AbstractBaseUser
from .forms import UserUpdateForm

# Create your views here.#

@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def related_products(request, slug):
    product = get_object_or_404(Product, slug=slug)
    sub_category = product.sub_category  # Get the subcategory of the product
    related_products = Product.objects.filter(sub_category=sub_category).exclude(slug=slug)[:5]
    serializer = ProductSerializer(related_products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def review_list(request, slug):
    product = get_object_or_404(Product, slug=slug)
    reviews = Review.objects.filter(product=product)
    total_reviews_count = reviews.count()
    serializer = ReviewSerializer(reviews, many=True)
    response_data = {
        'total_reviews_count': total_reviews_count,
        'reviews': serializer.data
    }

    return Response(response_data)


@api_view(['GET'])
def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    serializer = CategorySerializer(category)
    return Response(serializer.data)


@api_view(['GET'])
def Offer_list(request):
    offers = Offer.objects.all()
    serializer = OfferSerializer(offers, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def Category_list(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def newsletter(request):
    serializer = NewsletterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
    
@api_view(['POST'])
def add_cart(request):
    serializer = CartItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
    
@api_view(['GET'])
def get_subcategories(request,category_id):
    try:
        subcategories = SubCategory.objects.filter(category_id=category_id)
        serializer = SubCategorySerializer(subcategories, many=True)
        response_data = serializer.data
    except SubCategory.DoesNotExist:
        response_data = []

    return Response(response_data)


@api_view(['POST'])
def like_create(request):
    serializer = LikeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def dislike_create(request):
    serializer = DislikeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

