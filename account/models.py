from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext as _

from userena.models import UserenaLanguageBaseProfile


class Profile(UserenaLanguageBaseProfile):
    user = models.OneToOneField(User,
                                unique=True,
                                verbose_name=_('user'),
                                related_name='profile')
    city = models.CharField(_('city'), max_length=50, blank=True)
    about_me = models.TextField(_('about me'), blank=True)
    website = models.URLField(_('website'), blank=True)

    class Meta:
        verbose_name = _('profile')
        verbose_name_plural = _('profiles')

    def __unicode__(self):
        return self.user.username
