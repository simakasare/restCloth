from django.db.models.query import QuerySet
from django.shortcuts import render

from .serializers import *
from .models import Category,Product
from rest_framework import status
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse

from rest_framework.decorators import api_view



# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/product-list/',
		'Detail View':'/product-detail/<str:pk>/',
		'Create':'/product-create/',
		'Update':'/product-update/<str:pk>/',
		'Delete':'/product-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def productList(request):
	
	
        
       
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset , many = True)
        return Response({'responseData' :serializer.data})
    
	
	


@api_view(['GET'])
def productDetail(request, pk):
	
        
       
        queryset = Product.objects.get(id=pk)
        serializer = ProductSerializer(queryset , many = False)
        return Response({'responseData' :serializer.data})

	    
	


@api_view(['POST'])
def productCreate(request):
	
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset , data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)


	

@api_view(['POST'])
def productUpdate(request, pk):
	queryset =Product.objects.get(id=pk)
	serializer = ProductSerializer(instance=queryset, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def productDelete(request, pk):
	queryset = Product.objects.get(id=pk)
	queryset.delete()

	return Response('Item succsesfully delete!')


	

