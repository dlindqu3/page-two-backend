from django.urls import path 
from . import views

urlpatterns = [
  # base url /api/
  # example: http://127.0.0.1:8000/api/reviews/hardcover-fiction
  path('reviews/<str:category>', views.get_current_list_by_category, name='get_current_list_by_category'),
]

# example list categories -- "list_name_encoded": 
# [
#   "combined-print-and-e-book-fiction", 
#   "combined-print-and-e-book-nonfiction",
#   "hardcover-fiction", 
#   'etc.'
# ]