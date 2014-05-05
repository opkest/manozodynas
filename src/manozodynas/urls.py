from django.conf.urls import patterns, url
from django.conf import settings

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .views import index_view
from .views import words_view
from .views import NewWord

urlpatterns = patterns('',
    url(r'^$', index_view, name='index'),
    url(r'^words/$', words_view, name='words_view'),
    url(r'^enter/$', NewWord.as_view(), name='enter_word'),
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
     {'document_root': settings.MEDIA_ROOT}),
)
