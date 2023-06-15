from rest_framework.response import Response
from rest_framework.decorators import api_view
from restbase.models import Favourite, Product, ViewHistory, SearchHistory, VisitHistory, Like
from ..serializers import FavouriteSerializer, ProductSerializer, SearchHistorySerializer, ViewHistorySerializer, VisitHistorySerializer, LikeSerializer
from rest_framework import status

@api_view(['GET', 'POST'])
def viewHistory(request):
    username = None
    if request.method == 'POST':
        product_id = request.data['product_id']
        view = ViewHistory(username=username, product_id= product_id)
        view.save()
        return Response(status=status.HTTP_200_OK)
    else:
        views = ViewHistory.objects.filter(username=username)
        ids = []
        for view in views:
            ids.append(view.product_id)
        products = Product.objects.filter(id__in=ids)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def visitHistory(request):
    username = None
    if request.method == 'POST':
        product_id = request.data['product_id']
        visit = VisitHistory(username=username, product_id= product_id)
        visit.save()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', 'GET'])
def searchHistory(request):
    username = None
    if request.method == 'POST':
        search_query =  request.data['search_query']
        search = SearchHistory(username=username, search_query= search_query)
        search.save()
        return Response(status=status.HTTP_200_OK)
    else:
        searches = SearchHistory.objects.filter(username=username)
        serializer = SearchHistorySerializer(searches, many=True)
        return Response(serializer.data)


@api_view(['POST', 'GET'])
def favourite(request):
    username = None
    if request.method == 'POST':
        product_id = request.data['product_id']
        favourite = Favourite(username=username, product_id=product_id)
        favourite.save()
        return Response(status=status.HTTP_200_OK)
    else:
        favourites = Favourite.objects.filter(username=username)
        ids = []
        for favourite in favourites:
            ids.append(favourite.product_id)
        products = Product.objects.filter(id__in=ids)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
@api_view(['POST', 'GET'])
def like(request):
    username = None
    if request.method == 'POST':
        product_id = request.data['product_id']
        like = Like(username=username, product_id=product_id)
        like.save()
        return Response(status=status.HTTP_200_OK)
    else:
        likes = Like.objects.filter(username=username)
        ids = []
        for like in likes:
            ids.append(like.product_id)
        products = Product.objects.filter(id__in=ids)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    