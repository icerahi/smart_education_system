from django.urls import path

from apps.node import views

urlpatterns=[
    path('',views.NodeListAndCreateView.as_view(),name='node'),
    path('<pk>/<slug>',views.NodeDetailAndUpdateView.as_view(),name='node_detail')
]