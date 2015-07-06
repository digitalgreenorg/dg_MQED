from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

import coco.urls

from django.contrib import admin
admin.autodiscover()

from coco.data_log import send_updated_log
from coco_admin import coco_admin

urlpatterns = patterns('',
    url(r'', include('social.apps.django_app.urls', namespace='social')),
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATIC_DOC_ROOT, 'show_indexes': True}),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(coco_admin.urls)),
    (r'^coco/', include(coco.urls)),
    (r'^analytics/', include('output.urls')),
    
    (r'^get_log/?$', send_updated_log),
    # End imports from dashboard
    (r'^coco/docs/', TemplateView.as_view(template_name='cocodoc.html')),
    
)

# Static files serving locally
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
