from serpapi import GoogleSearch
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import permissions
from potw_api.models import Place
from potw_api.serializers import *

@api_view(['POST'])
def places(request):
    data = request.data
    serializer = PlaceRequestSerializer(data=data)
    if serializer.is_valid():
        
        places = Place.objects.filter(genres__contains =  data['genres'])
        serialized_data = PlaceSerializer(places, many=True)
  
        return Response({"places": serialized_data.data}, status=status.HTTP_200_OK)
    
    return Response({"message":"Please provide a valid request data"}, status=400)


@api_view(['POST'])
def sync_user(request):
    data = request.data
    serializer = UserCreateSerializer(data = data)
    print('data', request.data)
    if serializer.is_valid():

        user = serializer.save()
        return Response({
            'message': 'User created successfully',
            'user': serializer.data
        }, status=status.HTTP_201_CREATED)

    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
