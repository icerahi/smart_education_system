"""smart_education_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(('apps.dashboard.urls','dashboard'),namespace='dashboard')),
    path('school/', include(('apps.school.urls', 'school'), namespace='school')),
    path('teacher/',include(('apps.teacher.urls','teacher'),namespace='teacher')),
    path('course_material/',include(('apps.course_material.urls','course_material'),namespace='course_material')),
    path('notice/',include(('apps.notice.urls','notice'),namespace='notice')),
    path('class_routine/',include(('apps.class_routine.urls','class_routine'),namespace='class_routine')),
    path('node/',include(('apps.node.urls','node'),namespace='node')),
    #thirdparty
    path('chaining/', include('smart_selects.urls')),

]

urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)