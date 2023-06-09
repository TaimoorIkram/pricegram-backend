from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from restbase.models import Product, Favourite, ViewHistory, SearchHistory, VisitHistory
from .serializers import ProductSerializer, FavouriteSerializer, SearchHistorySerializer, ViewHistorySerializer, VisitHistorySerializer
from django.db.models import Q


@api_view(['GET'])
def getAllRoutes(request):
    return Response({
        "getAllProducts/": "Gives all the products",
        "product/<int:id>/": "Gives the product by id",
        "products/": "Gives the products based on search results",
        "search/": "records search history of a user",
        "view/": "records when a user views a product",
        "visit/": "records when a user visits the external link of the product",
        "favourite/": "records the favourite products of a user"
    })


@api_view(['GET'])
def getAllProducts(request):
    person = Product.objects.all()[:25]
    serializer = ProductSerializer(person, many=True)
    return Response(serializer.data)


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
    print(params)
    products = Product.objects.filter(params)[:25]
    serializer = ProductSerializer(products, many=True)
    data = serializer.data
    return Response(data)


@api_view(['GET'])
def getProductById(request, id):
    products = Product.objects.get(id=id)
    serializer = ProductSerializer(products)
    data = serializer.data
    return Response(data)


@api_view(['GET', 'POST'])
def viewHistory(request):
    if request.method == 'POST':
        view = ViewHistorySerializer(request.data)
        if view.is_valid():
            view.save()
            return Response(status=status.HTTP_200_OK)
    else:
        username = 'username'
        products = Product.objects.get(username=username)
        serializer = ProductSerializer(products)
        data = serializer.data
        return Response(data)


@api_view(['POST'])
def visitHistory(request):
    visit = VisitHistory(request.data)
    if visit.is_valid():
        visit.save()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', 'GET'])
def searchHistory(request):
    if request.method == 'POST':
        search = SearchHistorySerializer(request.data)
        if search.is_valid():
            search.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        username = 'username'
        products = Product.objects.filter(username=username)
        serializer = ProductSerializer(products)
        data = serializer.data
        return Response(data)


@api_view(['POST', 'GET'])
def favourite(request):
    if request.method == 'POST':
        favourite = FavouriteSerializer(request.data)
        if favourite.is_valid():
            favourite.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        username = 'username'
        favourites = Product.objects.filter(username=username)
        serializer = FavouriteSerializer(favourites)
        data = serializer.data
        return Response(data)
