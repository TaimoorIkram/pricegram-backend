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
        username = request.data['username'] if request.data['username'] != None else None
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
    username = 'tammy'
    if request.method == 'POST':
        product_id = request.data['product_id']
        username = request.data['username'] if request.data['username'] != None else None
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
        username = request.data['username'] if request.data['username'] != None else None
        search = SearchHistory(username=username, search_query= search_query)
        search.save()
        return Response(status=status.HTTP_200_OK)
    else:
        searches = SearchHistory.objects.filter(username=username)
        serializer = SearchHistorySerializer(searches, many=True)
        return Response(serializer.data)


@api_view(['POST', 'GET', 'DELETE'])
def favourite(request):
    username = 'tammy'
    if request.method == 'POST':
        product_id = request.data['product_id']
        username = request.data['username'] if request.data['username'] != None else None
        favourite = Favourite(username=username, product_id=product_id)
        favourite.save()
        return Response(status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        product_id = request.data['product_id']
        username = request.data['username'] if request.data['username'] != None else None
        favourites = Favourite.objects.get(username=username, product_id=product_id)
        favourites.delete()
        return Response(status=status.HTTP_200_OK)
    else:
        favourites = Favourite.objects.filter(username=username)
        ids = []
        for favourite in favourites:
            ids.append(favourite.product_id)
        products = Product.objects.filter(id__in=ids)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
@api_view(['POST', 'GET', 'DELETE'])
def like(request):
    username = 'tammy'
    if request.method == 'POST':
        product_id = request.data['product_id']
        username = request.data['username'] if request.data['username'] != None else None
        like = Like(username=username, product_id=product_id)
        like.save()
        return Response(status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        product_id = request.data['product_id']
        username = request.data['username'] if request.data['username'] != None else None
        like = Like.objects.get(username=username, product_id=product_id)
        like.delete()
        return Response(status=status.HTTP_200_OK)
    else:
        likes = Like.objects.filter(username=username)
        ids = []
        for like in likes:
            ids.append(like.product_id)
        products = Product.objects.filter(id__in=ids)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

@api_view(['POST', 'GET'])
def unitLike(request, user, id):
    try:
        likes = Like.objects.get(username=user, product_id=id)
        serializer = LikeSerializer(likes, many=False)
        return Response(serializer.data)
    except: return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST', 'GET'])
def unitFavourite(request, user, id):
    try:
        favourites = Favourite.objects.get(username=user, product_id=id)
        serializer = FavouriteSerializer(favourites, many=False)
        return Response(serializer.data)
    except: return Response(status=status.HTTP_404_NOT_FOUND)
    