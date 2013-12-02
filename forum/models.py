from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext as _


class Node(models.Model):

    name = models.CharField(_('name'), max_length=50, unique=True)
    description = models.TextField(_('description'))

    num_topics = models.IntegerField(_('number of topics'), default=0)

    created_on = models.DateTimeField(_('created on'), auto_now_add=True)
    updated_on = models.DateTimeField(_('updated on'), blank=True, null=True)

    class Meta:
        verbose_name = _('node')
        verbose_name_plural = _('nodes')

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('node_detail', kwargs={'name_slug': self.name})


class Topic(models.Model):

    author = models.ForeignKey(User,
                               verbose_name=_('author'),
                               related_name='topics')

    author_ip = models.IPAddressField(_('author\'s ip'), blank=True, null=True)

    node = models.ForeignKey(Node,
                             verbose_name=_('node'),
                             related_name='topics')

    title = models.CharField(_('title'), max_length=50)
    content = models.TextField(_('content'))

    num_hits = models.IntegerField(_('number of hits'), default=0)
    num_replies = models.IntegerField(_('number of replies'), default=0)

    last_reply_on = models.DateTimeField(_('last reply on'),
                                         blank=True, null=True)

    locked = models.BooleanField(_('locked'), default=False)
    sticky = models.BooleanField(_('sticky'), default=False)

    created_on = models.DateTimeField(_('created on'), auto_now_add=True)
    updated_on = models.DateTimeField(_('updated on'), blank=True, null=True)

    class Meta:
        verbose_name = _('topic')
        verbose_name_plural = _('topics')
        get_latest_by = 'created_on'
        ordering = ['-last_reply_on']

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('topic_detail', kwargs={'pk': self.id})


class Reply(models.Model):

    author = models.ForeignKey(User,
                               verbose_name=_('author'),
                               related_name='replies')

    author_ip = models.IPAddressField(_('author\'s ip'), blank=True, null=True)

    topic = models.ForeignKey(Topic,
                              verbose_name=_('topic'),
                              related_name='replies')

    content = models.TextField(_('content'))

    created_on = models.DateTimeField(_('created on'), auto_now_add=True)
    updated_on = models.DateTimeField(_('updated on'), blank=True, null=True)

    class Meta:
        verbose_name = _('reply')
        verbose_name_plural = _('replies')
