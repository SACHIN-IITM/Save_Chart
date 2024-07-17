# urls.py (main project)

from django.conf.urls import include, url

urlpatterns = [
    url(r'^1\.1/', include('api.v11.urls')),  # Matches /1.1/charts
    url(r'', include('django_prometheus.urls')),  # Assuming this is for metrics, adjust if necessary
]
