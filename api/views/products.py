from rest_framework.response import Response
from rest_framework.decorators import api_view
from restbase.models import Product, SearchHistory, ViewHistory
from ..serializers import ProductSerializer, ReviewSerializer
from django.db.models import Q
from rest_framework import status
from django.core.paginator import Paginator
from ..pricegram_search.engine_instance import engine

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
    except:
        pass

    keywords = []
    for keyword_list in zip(filters.keys(), filters.values()):
        for keyword in keyword_list[1]:
            if keyword_list[0] != 'page':
                keywords.append(keyword)
    search = SearchHistory(username=username, search_query=search_query)
    search.save()

# LOADING THE PIPELINE AND VECTORS
    
    results = engine.search(
        keywords=keywords,
        cluster_size=30,
        k=100,
    )

    """
    products = Product.objects.all()[:500]
    serializer = ProductSerializer(products, many=True)
    data = serializer.data
    """

    page_number = request.query_params.get("page")
    if page_number == None:
        page_number = 1
    paginator = Paginator(results, 40)
    total_pages = paginator.num_pages
    page_obj = paginator.page(page_number)
    products = page_obj.object_list
    return Response({
        'products': products,
        'totalPages': total_pages
    })
