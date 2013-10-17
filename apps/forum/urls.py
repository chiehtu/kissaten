from django.conf.urls import patterns, include, url

from forum.views import ForumIndexView, TopicDetailView


topic_patterns = patterns(
    '',
    url(r'^(?P<pk>\d+)/$', TopicDetailView.as_view(), name='topic_detail'),
)

urlpatterns = patterns(
    '',
    url(r'^$', ForumIndexView.as_view(), name='forum_index'),
    (r'^topic/', include(topic_patterns)),
)
