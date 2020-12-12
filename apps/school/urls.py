from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.SchoolCreateAndListView.as_view(),name='school'),
    path('<int:pk>/<slug>/',views.SchoolDetailAndUpdateView.as_view(),name='school_detail'),
]
