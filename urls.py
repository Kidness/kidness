# python imports
import os

# django imports
from django.conf.urls.defaults import *
from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.views.generic.simple import direct_to_template
from kidness.views import *

admin.autodiscover()
DIRNAME = os.path.dirname(__file__)

handler500 = 'lfc.views.fiveohoh'

urlpatterns = patterns('',
    (r'PIE.htc$', 'kidness.views.handle_htc_file'),
)
# Django 
urlpatterns += patterns('',
    url('^accounts/login/?$', login, {"template_name" : "admin/login.html"}, name='auth_login'),
    url('^accounts/logout/?$', logout, name='auth_logout'),

    (r'^admin/(.*)', admin.site.root),
    (r'^jsi18n/$', 'django.views.i18n.javascript_catalog', {'packages': ('django.conf') }),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(DIRNAME, "media"), 'show_indexes': True }),
)

urlpatterns += patterns("",
    url(r'^vklogin/?$', vklogin),
    url(r'^opinion-save$', save_opinion),
    url(r'^consult-form$', consult_form)
)

# LFC Blog
urlpatterns += patterns("",
    (r'', include('lfc_blog.urls')),
)

# LFC
urlpatterns += patterns('',
    (r'^manage/', include('lfc.manage.urls')),
    (r'', include('lfc.urls')),
)