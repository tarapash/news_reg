from django.contrib import admin
from django.urls import path, include

urlpatterns = [
   path('admin/', admin.site.urls),
   path('sign/', include('sign.urls')),
   path('accounts/', include('allauth.urls')),
   path('posts/', include('Portal_app.urls')),
]

   

