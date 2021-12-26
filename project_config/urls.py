from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
]

v1_0 = 'api/v1/'

v1_0_urls = [
    path(v1_0, include(('organization.urls', 'organization_1_0'))),
]

urlpatterns += v1_0_urls
