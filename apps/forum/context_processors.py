from django.contrib.auth.models import User
from django.contrib.sites.models import Site

from forum.models import Topic, Reply


def site_info(request):
    return {'site': Site.objects.all()[0]}


def site_statistics(request):
    statistics = {}
    statistics['num_members'] = User.objects.count()
    statistics['num_topics'] = Topic.objects.count()
    statistics['num_replies'] = Reply.objects.count()

    return statistics
