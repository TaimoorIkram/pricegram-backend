from rest_framework.response import Response
from rest_framework.decorators import api_view
from restbase.models import Favourite, ViewHistory, SearchHistory, VisitHistory, Like
from .serializers import FavouriteSerializer, SearchHistorySerializer, ViewHistorySerializer, VisitHistorySerializer, LikeSerializer
from rest_framework import status

@api_view(['GET', 'POST'])
def viewHistory(request):
    username = None
    if request.method == 'POST':
        product_id = request.POST['product_id']
        view = ViewHistory(username=username, product_id= product_id)
        view.save()
        return Response(status=status.HTTP_200_OK)
    else:
        views = ViewHistory.objects.filter(username=username)
        serializer = ViewHistorySerializer(views, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def visitHistory(request):
    username = None
    if request.method == 'POST':
        product_id = request.POST['product_id']
        visit = VisitHistory(username=username, product_id= product_id)
        visit.save()
        return Response(status=status.HTTP_200_OK)
    else:
        visits = VisitHistory.objects.filter(username=username)
        serializer = VisitHistorySerializer(visits, many=True)
        return Response(serializer.data)


@api_view(['POST', 'GET'])
def searchHistory(request):
    username = None
    if request.method == 'POST':
        search_query = request.POST['q']
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
        product_id = request.POST['product_id']
        favourite = Favourite(username=username, product_id=product_id)
        favourite.save()
        return Response(status=status.HTTP_200_OK)
    else:
        favourites = Favourite.objects.filter(username=username)
        serializer = FavouriteSerializer(favourites, many=True)
        return Response(serializer.data)
    
@api_view(['POST', 'GET'])
def like(request):
    username = None
    if request.method == 'POST':
        product_id = request.POST['product_id']
        favourite = Like(username=username, product_id=product_id)
        favourite.save()
        return Response(status=status.HTTP_200_OK)
    else:
        favourites = Like.objects.filter(username=username)
        serializer = LikeSerializer(favourites, many=True)
        return Response(serializer.data)