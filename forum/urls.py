from django.conf.urls import patterns, include, url

from forum.views.base import MarkdownView

from forum.views.node import (NodeIndexView, NodeCreateView,
                              NodeEditView, NodeDetailView)
from forum.views.topic import (ForumIndexView, TopicCreateView,
                               TopicDetailView, TopicEditView)
from forum.views.reply import ReplyCreateView, ReplyEditView
from forum.feeds import LatestTopicsFeed


topic_patterns = patterns(
    '',
    url(r'^create/$', TopicCreateView.as_view(), name='topic_create'),
    url(r'^(?P<pk>\d+)/$', TopicDetailView.as_view(), name='topic_detail'),
    url(r'^(?P<pk>\d+)/edit/$', TopicEditView.as_view(), name='topic_edit'),
    url(r'^(?P<pk>\d+)/reply/$', ReplyCreateView.as_view(),
        name='reply_create'),
    url(r'^\d+/reply/(?P<pk>\d+)/$', ReplyEditView.as_view(),
        name='reply_edit'),
)

node_patterns = patterns(
    '',
    url(r'^$', NodeIndexView.as_view(), name='node_index'),
    url(r'^create/$', NodeCreateView.as_view(), name='node_create'),
    url(r'^(?P<name_slug>\w+)/$', NodeDetailView.as_view(),
        name='node_detail'),
    url(r'^(?P<name_slug>\w+)/edit/$', NodeEditView.as_view(),
        name='node_edit')

)

urlpatterns = patterns(
    '',
    url(r'^$', ForumIndexView.as_view(), name='forum_index'),
    (r'^topic/', include(topic_patterns)),
    (r'^node/', include(node_patterns)),
    (r'^markdown/$', MarkdownView.as_view()),
    (r'^feed/$', LatestTopicsFeed()),
)
