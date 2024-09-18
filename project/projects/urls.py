from django.urls import path 
from .views import ProjectListView , ProjectCreateView

urlpatterns = [

    path('',ProjectListView.as_view(), name='Project_list'),
    path('create',ProjectCreateView.as_view(), name='Project_Create')

]