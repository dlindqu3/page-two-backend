from rest_framework import serializers
from .models import CurrentBestSellersListItem

class CurrentBestSellersListItemSerializer(serializers.ModelSerializer): 
  class Meta: 
    model = CurrentBestSellersListItem
    fields = "__all__"