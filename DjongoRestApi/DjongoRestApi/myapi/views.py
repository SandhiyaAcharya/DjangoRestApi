
from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from myapi import serializers
from myapi.models import Mypost
from myapi.serializers import MypostSerializer 
from rest_framework.decorators import api_view
from pymongo import MongoClient
# Create your views here.


client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.bezkoder
collection = db.myapi_mypost



@api_view(['GET', 'POST', 'DELETE'])
def list(request):
    if request.method == 'GET':
        mypost = Mypost.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            mypost = mypost.filter(title__icontains=title)
        
        mypost_serializer = MypostSerializer(mypost, many=True)
        return JsonResponse(mypost_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        post_data = JSONParser().parse(request)
        mypost_serializer = MypostSerializer(data=post_data)
        if mypost_serializer.is_valid():
            mypost_serializer.save()
            return JsonResponse(mypost_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(mypost_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Mypost.objects.all().delete()
        return JsonResponse({'message': '{} post were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 

@api_view(['GET', 'PUT', 'DELETE','PATCH'])
def detail(request, pk):
    try: 
        mypost = Mypost.objects.get(pk=pk) 
    except Mypost.DoesNotExist: 
        return JsonResponse({'message': 'The Mypost does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        mypost_serializer = MypostSerializer(mypost) 
        return JsonResponse(mypost_serializer.data) 
 
    elif request.method == 'PUT': 
        post_data = JSONParser().parse(request) 
        mypost_serializer = MypostSerializer(mypost, data=post_data) 
        if mypost_serializer.is_valid(): 
            mypost_serializer.save() 
            return JsonResponse(mypost_serializer.data) 
        return JsonResponse(mypost_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        mypost.delete() 
        return JsonResponse({'message': 'Post was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

    elif request.method=='PATCH':
        #  like_object=Mypost.object.get()
         data=request.data
         mypost.Pusername=data.get('Pusername',mypost.Pusername)
         mypost.title=data.get('title',mypost.title)
         mypost.description=data.get('description',mypost.description)
         mypost.like=data.get('like',mypost.like)
         mypost.TotalLike=data.get('TotalLike',mypost.TotalLike)

         mypost.save()
         serializer=MypostSerializer(mypost)
         return JsonResponse(serializer.data)

def patch(request):
     like_object=Mypost.object.get()
     data=request.data
     like_object.Pusername=data.get('Pusername',like_object.Pusername)
     like_object.title=data.get('title',like_object.title)
     like_object.description=data.get('description',like_object.description)
     like_object.like=data.get('like',like_object.like)
     like_object.TotalLike=data.get('TotalLike',like_object.TotalLike)

     like_object.save()
     serializer=MypostSerializer(like_object)
     return JsonResponse(serializer.data)