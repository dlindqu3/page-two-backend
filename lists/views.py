from django.shortcuts import render
from django.http import JsonResponse
# the HttpResponse module allows you to return stuff without a template  
import requests 
import os
from .models import CurrentBestSellersListItem
from datetime import date
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CurrentBestSellersListItemSerializer



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
# create a saved item 
@api_view(['POST'])
def create_saved_list_item(item_data): 
  serializer = CurrentBestSellersListItemSerializer(data=item_data)
  # if serializer is valid, send to db 
  if serializer.is_valid(): 
    serializer.save()
  return Response(serializer.data)

# read/get all saved lists' items 
@api_view(['GET'])
def all_saved_lists_items(request): 
  all_lists_items = CurrentBestSellersListItem.objects.all()
  serializer = CurrentBestSellersListItemSerializer(all_lists_items, many=True)
  return Response(serializer.data)

# read/get a single list item's detail 
@api_view(['GET'])
def saved_list_item_detail(request, pk): 
  list = CurrentBestSellersListItem.objects.get(id=pk)
  serializer = CurrentBestSellersListItemSerializer(list, many=False)
  return Response(serializer.data)

# delete single list item 
@api_view(['DELETE'])
def item_delete(request, pk): 
  item = CurrentBestSellersListItem.objects.get(id=pk)
  item.delete()
  
  return Response('saved list item deleted')