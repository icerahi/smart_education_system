from django.urls import path

from apps.course_material import views

urlpatterns=[
    path('',views.CourseMaterialCreateAndListView.as_view(),name='course_material'),
    path('<class_name>/<subject>',views.get_content,name='get_content'),
]