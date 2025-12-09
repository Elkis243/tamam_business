"""
URL configuration for tamam_business project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from app import error_handlers
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
]

# Custom error handlers
handler400 = error_handlers.handler400
handler403 = error_handlers.handler403
handler404 = error_handlers.handler404
handler500 = error_handlers.handler500
