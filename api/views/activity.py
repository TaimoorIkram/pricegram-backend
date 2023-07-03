from rest_framework.response import Response
from rest_framework.decorators import api_view
from restbase.models import Favourite, Product, Review, ViewHistory, SearchHistory, VisitHistory, Like
from ..serializers import FavouriteSerializer, ProductSerializer, SearchHistorySerializer, LikeSerializer, ReviewSerializer
from rest_framework import status

@api_view(['GET'])
def viewHistory(request):
    username = request.user.username
    if request.method == 'GET':
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

@api_view(['GET'])
def searchHistory(request):
    username = request.user.username
    if request.method == 'GET':
        print(username,'searchHistory GET') 
        searches = SearchHistory.objects.filter(username=username)
        serializer = SearchHistorySerializer(searches, many=True)
        return Response(serializer.data)


@api_view(['POST', 'GET'])
def favourite(request):
    username = request.user.username
    if request.method == 'POST':
        print(username,'favourite POST') 
        product_id = request.data['product_id']
        favourite = Favourite(username=username, product_id=product_id)
        favourite.save()
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
    
@api_view(['POST', 'GET'])
def like(request):
    username = request.user.username
    if request.method == 'POST':
        print(username,'like POST') 
        product_id = request.data['product_id']
        like = Like(username=username, product_id=product_id)
        like.save()
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

@api_view(['GET'])
def unitLike(request,id):
    try:
        username = request.user.username
        likes = Like.objects.get(username=username, product_id=id)
        serializer = LikeSerializer(likes, many=False)
        return Response(serializer.data)
    except: return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def unitFavourite(request,id):
    try:
        username = request.user.username
        favourites = Favourite.objects.get(username=username, product_id=id)
        serializer = FavouriteSerializer(favourites, many=False)
        return Response(serializer.data)
    except: return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['DELETE'])
def unlike(request, id):
    username = request.user.username
    print(username,'like DELETE') 
    like = Like.objects.get(username=username, product_id=id)
    like.delete()
    return Response(status=status.HTTP_200_OK)

@api_view(['DELETE'])
def removeFromFavourites(request, id):
    username = request.user.username
    print(username,'favourite DELETE') 
    favourites = Favourite.objects.get(username=username, product_id=id)
    favourites.delete()
    return Response(status=status.HTTP_200_OK)

@api_view(['POST'])
def insertReview(request):
    username = request.user.username
    id = request.data['id']
    rating = request.data['rating']
    comment = request.data['comment']
    review = Review(product_id = id, username = username, average_rating=rating, comment=comment)
    review.save()
    return Response(status=status.HTTP_200_OK)
    
        