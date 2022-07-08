from django.shortcuts import render
from django.http import JsonResponse
# the HttpResponse module allows you to return stuff without a template  
import requests 
import os
from .models import CurrentBestSellersListItem
from datetime import date
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from .serializers import CurrentBestSellersListItemSerializer
import json
from rest_framework.renderers import JSONRenderer


nyt_key = os.environ.get('NYT_KEY')

# Create your views here.
def get_current_list_by_category(request, category): 

  url = f'https://api.nytimes.com/svc/books/v3/lists/current/{category}.json?api-key={nyt_key}'
  
  response = requests.get(url)
  data = response.json()
  t1 = data['results']['books'][0]['title']
  a1 = data['results']['books'][0]['author']
  result = f'{a1}: {t1}'
 
  return JsonResponse(result, safe=False)

# methods 
  # create a saved item 
  # read/get all saved lists' items 
  # read/get a single list item's detail 
  # no update 
  # delete single list item 
# require a user action after API call to create/save a particular item 

#fix 


{
"rank": 555, 
"weeks_on_list": 555, 
"publisher": "a", 
"description": "b", 
"title": "c", 
"author": "d",
"amazon_product_url": "https://amazon.com/books/"
}

# create a saved item 
@api_view(['GET', 'POST'])
def create_saved_list_item(request):
  if request.method == 'POST':
    serializer = CurrentBestSellersListItemSerializer(data=request.data,  many=False)
    
    if serializer.is_valid(): 
      serializer.save()
      return Response(serializer.data)
    else:
      return JsonResponse({'errors': serializer.errors, 'input_data': request.data, 'validated_data': serializer.validated_data})
  
  return Response('res')


# read/get all saved lists' items 
@api_view(['GET'])
def get_all_saved_lists_items(request): 
  all_lists_items = CurrentBestSellersListItem.objects.all()
  serializer = CurrentBestSellersListItemSerializer(all_lists_items, many=True)
  return Response(serializer.data)

# read/get a single list item's detail 
@api_view(['GET'])
def get_saved_list_item_detail(request, pk): 
  list = CurrentBestSellersListItem.objects.get(id=pk)
  serializer = CurrentBestSellersListItemSerializer(list, many=False)
  return Response(serializer.data)

# delete single list item 
@api_view(['DELETE', 'GET'])
def item_delete(request, pk): 
  item = CurrentBestSellersListItem.objects.get(id=pk)
  item.delete()
  
  return Response('saved list item deleted')
