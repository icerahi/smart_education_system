from django.urls import path

from apps.teacher import views

urlpatterns=[
    path('',views.TeacherCreateAndListView.as_view(),name='teacher'),
    path('<pk>/<slug>',views.TeacherDetailAndUpdateView.as_view(),name = 'teacher_detail'),

 ]