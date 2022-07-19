from django.urls import path 
from . import views

urlpatterns = [
  # base url /api/
  # example: http://127.0.0.1:8000/api/lists/hardcover-fiction
  path('lists/<str:category>/', views.get_current_list_by_category, name='get_current_list_by_category'),


  path('lists-items/', views.get_all_saved_lists_items, name='get_all_saved_lists_items'),
  path('item-detail/<str:pk>/', views.get_saved_list_item_detail, name='get_saved_list_item_detail'),


   path('list-item-create/', views.create_saved_list_item, name='create_saved_list_item'),

   # don't need update 
  path('item-delete/<str:pk>/', views.item_delete, name='item_delete'),

]

# example list categories -- "list_name_encoded": 
# [
#   "combined-print-and-e-book-fiction", 
#   "combined-print-and-e-book-nonfiction",
#   "hardcover-fiction", 
#   'etc.'
# ]