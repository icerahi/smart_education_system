from django.urls import path

from apps.node import views

urlpatterns=[
    path('',views.NodeListAndCreateView.as_view(),name='node'),
    path('<pk>/',views.NodeDetailAndUpdateView.as_view(),name='node_detail'),
    path('status/<pk>/',views.enable_disable,name='enable_disable'),
]