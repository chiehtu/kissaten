from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse

from django_misaka.templatetags.markdown import markdown

from forum.models import Topic

class LatestTopicsFeed(Feed):
    title = ""
    link = ""
    description = ""


    def items(self):
        return Topic.objects.order_by('-created_on')[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return markdown(item.content)

    def item_link(self, item):
        return reverse('topic_detail', args=[item.pk])
