from rest_framework.response import Response
from rest_framework.decorators import api_view
from restbase.models import Person
from .serializers import PersonSerializer

@api_view(['POST','GET'])
def getAllItems(request):
    person = Person.objects.all()
    serializer = PersonSerializer(person, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addPerson(request):
    serializer = PersonSerializer(data=request.data)
    if serializer.is_valid(): serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def getProducts(request):
    brand =  request.GET.get("brand")
    category = request.GET.get("category")
    vendor = request.GET.get("vendor")
    params = Q()
    if brand is not None:
        qbrand = Q(brand = brand)
        params &= qbrand
    if category is not None:
        qcategory = Q(category = category)
        params &= qcategory
    if vendor is not None:
        qvendor = Q(vendor = vendor)
        params &= qvendor
    print(params)
    products = Product.objects.filter(params)
    serializer = ProductSerializer(products, many = True)
    data = serializer.data
    return Response(data)

@api_view(['GET'])
def getProduct(request, id):
    products = Product.objects.get(id = id)
    serializer = ProductSerializer(products)
    data = serializer.data
    return Response(data)