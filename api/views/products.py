from rest_framework.response import Response
from rest_framework.decorators import api_view
from restbase.models import Product, SearchHistory, ViewHistory
from ..serializers import ProductSerializer, ReviewSerializer
from django.db.models import Q
from rest_framework import status
from ..searchmodel.searchmodel import *


@api_view(['GET'])
def getAllRoutes(request):
    return Response({
        "all/": "Gives all the products",
        "product/<int:id>/": "Gives the product by id",
        "products/": "Gives the products based on filters",
        "search/": "Gives the products based on search results",
        "searches/": "records search history of a user",
        "view/": "records when a user views a product",
        "visit/": "records when a user visits the external link of the product",
        "favourite/": "records the favourite products of a user",
        "like/": "records the likes of the user"
    })


@api_view(['GET'])
def getAllProducts(request):
    products = Product.objects.all()[:25]
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data[:25])


@api_view(['GET'])
def getProductById(request, id):
    try:
        username = request.user.username
    except:
        username = None
    view = ViewHistory(username=username, product_id=id)
    view.save()
    product = Product.objects.prefetch_related('reviewss').get(id=id)
    product_serializer = ProductSerializer(product)
    reviews = list(product.reviewss.all())
    review_serializers = ReviewSerializer(reviews, many=True)
    serialized_reviews = [dict(item) for item in review_serializers.data]
    serialized_product = product_serializer.data
    serialized_product['reviewss'] = serialized_reviews
    return Response({
        "product": serialized_product,
    })


@api_view(['GET'])
def getProducts(request):
    brand = request.GET.get("brand")
    category = request.GET.get("category")
    vendor = request.GET.get("vendor")
    params = Q()
    if brand is not None:
        qbrand = Q(brand=brand)
        params &= qbrand
    if category is not None:
        qcategory = Q(category=category)
        params &= qcategory
    if vendor is not None:
        qvendor = Q(vendor=vendor)
        params &= qvendor
    products = Product.objects.filter(params)[:25]
    serializer = ProductSerializer(products, many=True)
    data = serializer.data
    return Response(data)


@api_view(['GET'])
def search(request):
    try:
        username = request.user.username
    except:
        username = None
    search_query = request.query_params.get("q")
    try:
        filters = dict(request.query_params)
        filters.pop('q', None)
    except:
        pass
    for key in filters.keys():
        filters[key] = " ".join(filters[key])
    print(filters)
    search = SearchHistory(username=username, search_query=search_query)
    search.save()
    recommendations = engine.search(
        query=search_query,
        filters=filters,
        k=100,
    )
    return Response(recommendations)


"""
    products = Product.objects.all()[:25]
    serializer = ProductSerializer(products, many=True)
    data = serializer.data
    return Response(data)
    
"""
