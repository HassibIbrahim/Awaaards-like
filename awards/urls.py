from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
 
urlpatterns=[
    url(r'^$',views.index,name='Index'),
    url(r'^create/profile$',views.create_profile, name='create-profile'),
    url(r'^new/project$',views.new_project, name='new-project'),
    url(r'^directory/',views.directory, name='directory'),
    url(r'^profile/',views.profile, name='profile'),
    url(r'^site/(\d+)',views.site,name='site'),
    url(r'^search/',views.search_results, name='search_results'),
]
 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)