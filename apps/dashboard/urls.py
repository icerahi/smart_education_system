
from django.urls import path
from django.views.generic import RedirectView

from . import views
urlpatterns = [
    path('',views.Dashboard.as_view(),name='dashboard'),
    path('dashboard/',RedirectView.as_view(url="/")),


]
