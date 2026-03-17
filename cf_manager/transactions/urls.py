from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_transaction, name='add'),
    path('edit/<int:pk>/', views.edit_transaction, name='edit'),
    path('delete/<int:pk>/', views.delete_transaction, name='delete'),

    # Справочники
    path('manage/<str:model_name>/', views.manage_dictionary, name='manage_dictionary'),
    path('manage/<str:model_name>/<int:pk>/', views.manage_dictionary, name='manage_dictionary_edit'),
    
    # AJAX
    path('ajax/load-categories/', views.ajax_load_categories, name='ajax_load_categories'),
    path('ajax/load-subcategories/', views.ajax_load_subcategories, name='ajax_load_subcategories'),
]