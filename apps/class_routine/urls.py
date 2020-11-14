from django.urls import path

from apps.class_routine import views

urlpatterns=[
    path('',views.RoutineCreateAndListView.as_view(),name='routine'),
    path('<class_name>/',views.GetRoutineView.as_view(),name='get_routine'),
]