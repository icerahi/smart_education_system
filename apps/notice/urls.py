from django.urls import path

from apps.notice import views

urlpatterns=[
    path('',views.NoticeListAndCreateView.as_view(),name='notice'),
    path('<pk>/',views.NoticeDetailAndUpdateView.as_view(),name='notice_detail'),
    path('<pk>/<status>/',views.notice_status,name='notice_status'),
]