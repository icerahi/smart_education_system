from django.urls import path

from apps.course_material import views

urlpatterns=[
    path('',views.CourseMaterialCreateAndListView.as_view(),name='course_material'),
]