from django.db import models

# Create your models here.
class CurrentBestSellersListItem(models.Model):
  rank = models.IntegerField(blank=True)
  weeks_on_list = models.IntegerField(blank=True)
  publisher = models.CharField(max_length=256, blank=True)
  description = models.CharField(max_length=500, blank=True)
  title = models.CharField(max_length=256, blank=True)
  author = models.CharField(max_length=256, blank=True)
  amazon_product_url = models.URLField(max_length=500, blank=True) 