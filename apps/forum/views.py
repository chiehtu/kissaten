from django.views.generic.detail import DetailView
from django.views.generic.dates import ArchiveIndexView

from forum.models import Topic


class ForumIndexView(ArchiveIndexView):
    model = Topic
    date_field = 'last_reply_on'
    allow_empty = True
    paginate_by = 10
    template_name = 'forum/index.html'


class TopicDetailView(DetailView):
    model = Topic
