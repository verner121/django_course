from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('client.urls', namespace='client')),
                  path('', include('mailings.urls', namespace='mailings')),
                  path('users', include('users.urls', namespace='users')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
