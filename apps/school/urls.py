from django.urls import path, include
from . import views

urlpatterns = [
    path('school/',views.SchoolCreateAndListView.as_view(),name='school'),
    path('school/<int:pk>/<slug>',views.SchoolDetailAndUpdateView.as_view(),name='school_detail'),
]
