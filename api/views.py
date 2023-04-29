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