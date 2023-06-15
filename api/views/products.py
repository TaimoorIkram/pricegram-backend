from rest_framework.response import Response
from rest_framework.decorators import api_view
from restbase.models import Product
from ..serializers import ProductSerializer
from django.db.models import Q

# Gives the routes of all API endpoints
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
    person = Product.objects.all()[:25]
    serializer = ProductSerializer(person, many=True)
    return Response(serializer.data[:25])

@api_view(['GET'])
def getProductById(request, id):
    products = Product.objects.get(id=id)
    serializer = ProductSerializer(products)
    data = serializer.data
    return Response(data)

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
    person = Product.objects.all()[:25]
    serializer = ProductSerializer(person, many=True)
    return Response(serializer.data)
    


