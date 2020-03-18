from django.contrib import admin
from django.urls import path, include
from records import views

urlpatterns = [
    #path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('', views.index),
]
