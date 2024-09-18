from django.urls import path 
from .views import (ProjectListView , ProjectCreateView , ProjectUpdateView , ProjectDeleteView
                    ,TaskCreateView , TaskUpdateView , TaskDeleteView)

urlpatterns = [

    path('',ProjectListView.as_view(), name='Project_list'),
    path('create',ProjectCreateView.as_view(), name='Project_Create'),
    path('edit/<int:pk>',ProjectUpdateView.as_view(), name='Project_Update'),
    path('edit/delete/<int:pk>',ProjectDeleteView.as_view(), name='Project_delete'),
    path('task/create',TaskCreateView.as_view(), name='Task_Create'),
    path('task/edit/<int:pk>',TaskUpdateView.as_view(), name='Task_update'),
    path('task/delete/<int:pk>',TaskDeleteView.as_view(), name='Task_delete'),

]