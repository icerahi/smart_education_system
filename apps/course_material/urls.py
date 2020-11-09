from django.urls import path

from apps.course_material import views

urlpatterns=[
    path('',views.CourseMaterialCreateAndListView.as_view(),name='course_material'),
    path('<class_name>/<subject>',views.GetContentView.as_view(),name='get_content'),
    path('edit/<class_name>/<subject>/<chapter>/<pk>',views.ContentUpdateView.as_view(),name='update_content'),
]