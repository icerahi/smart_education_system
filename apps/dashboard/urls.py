
from django.urls import path
from . import views
urlpatterns = [
    path('',views.Dashboard.as_view(),name='dashboard'),
    path('test/',views.MySelectView.as_view(),name='test'),

]
