from django.conf import settings
from django.contrib import admin
from django.urls import path , re_path, include
from django.conf.urls.static import serve





urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    re_path(r'^(?P<path>.*)$', serve, {'document_root': settings.FRONTEND_ROOT}),
    path('BookStore/', include('BookStore.urls')),
]
