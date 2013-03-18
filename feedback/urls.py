from django.conf.urls.defaults import patterns, include, url
from reflection.feedback.views import feedback


urlpatterns = patterns('',

	url(regex=r'^$',
		view=feedback,
		name='feedback',
	),
)