from django.urls import path

from apps.teacher import views

urlpatterns=[
      path('',views.IndexView.as_view(),name='teacher')
 ]