from rest_framework.response import Response
from rest_framework.decorators import api_view
from restbase.models import Favourite, Product, ViewHistory, SearchHistory, VisitHistory, Like
from ..serializers import FavouriteSerializer, ProductSerializer, SearchHistorySerializer, ViewHistorySerializer, VisitHistorySerializer, LikeSerializer
from rest_framework import status

@api_view(['GET', 'POST'])
def viewHistory(request):
    username = request.user.username
    if request.method == 'POST':
        print(username,'viewHistory POST')
        product_id = request.data['product_id']
        view = ViewHistory(username=username, product_id= product_id)
        view.save()
        return Response(status=status.HTTP_200_OK)
    else:
        print(username,'viewHistory GET')
        views = ViewHistory.objects.filter(username=username)
        ids = []
        for view in views:
            ids.append(view.product_id)
        products = Product.objects.filter(id__in=ids)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def visitHistory(request):
    username = request.user.username
    if request.method == 'POST':
        print(username,'visitHistory POST')
        product_id = request.data['product_id']
        visit = VisitHistory(username=username, product_id= product_id)
        visit.save()
        return Response(status=status.HTTP_200_OK)
    else:
        print(username,'visitHistory GET')
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', 'GET'])
def searchHistory(request):
    username = request.user.username
    if request.method == 'POST':
        print(username,'searchHistory POST') 
        search_query =  request.data['search_query']
        search = SearchHistory(username=username, search_query= search_query)
        search.save()
        return Response(status=status.HTTP_200_OK)
    else:
        print(username,'searchHistory GET') 
        searches = SearchHistory.objects.filter(username=username)
        serializer = SearchHistorySerializer(searches, many=True)
        return Response(serializer.data)


@api_view(['POST', 'GET', 'DELETE'])
def favourite(request):
    username = request.user.username
    if request.method == 'POST':
        print(username,'favourite POST') 
        product_id = request.data['product_id']
        favourite = Favourite(username=username, product_id=product_id)
        favourite.save()
        return Response(status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        print(username,'favourite DELETE') 
        product_id = request.data['product_id']
        # username = request.data['username'] if request.data['username'] != None else None
        favourites = Favourite.objects.get(username=username, product_id=product_id)
        favourites.delete()
        return Response(status=status.HTTP_200_OK)
    else:
        print(username,'favourite GET') 
        favourites = Favourite.objects.filter(username=username)
        ids = []
        for favourite in favourites:
            ids.append(favourite.product_id)
        products = Product.objects.filter(id__in=ids)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
@api_view(['POST', 'GET', 'DELETE'])
def like(request):
    username = request.user.username
    if request.method == 'POST':
        print(username,'like POST') 
        product_id = request.data['product_id']
        like = Like(username=username, product_id=product_id)
        like.save()
        return Response(status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        print(username,'like DELETE') 
        product_id = request.data['product_id']
        like = Like.objects.get(username=username, product_id=product_id)
        like.delete()
        return Response(status=status.HTTP_200_OK)
    else:
        print(username,'like GET') 
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
    