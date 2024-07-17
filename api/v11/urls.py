# api/v11/urls.py

from django.conf.urls import url
from . import studyTemplates, drawingTemplates, charts

urlpatterns = [
    url(r'^charts$', charts.processRequest),
    url(r'^study_templates$', studyTemplates.processRequest),
    url(r'^drawing_templates$', drawingTemplates.processRequest),
]
