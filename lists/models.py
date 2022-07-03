from django.db import models

# Create your models here.
class CurrentBestSellersListItem(models.Model):
  rank = models.IntegerField()
  weeks_on_list = models.IntegerField()
  publisher = models.CharField(max_length=256)
  description = models.CharField(max_length=500)
  title = models.CharField(max_length=256)
  author = models.CharField(max_length=256)
  amazon_product_url = models.URLField(max_length=500) 