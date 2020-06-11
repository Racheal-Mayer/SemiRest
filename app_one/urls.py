from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('addshow', views.addshow),
    path('edit/<int:show_id>', views.edit),
    path('process_edit/<int:show_id>', views.process_edit),
    path('delete/<int:show_id>', views.delete),
    path('show/<int:show_id>', views.show)
    
]