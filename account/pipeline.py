from django.contrib.auth.models import User
from guardian.shortcuts import assign, get_perms_for_model

from account.models import Profile


def create_profile(user=None, profile=None, *args, **kwargs):
    if not user:
        return

    if profile:
        return {'profile': profile}

    return {'profile': Profile.objects.get_or_create(user=user)[0]}


def set_guardian_permissions(user=None, profile=None, *args, **kwargs):
    if not user or user.is_authenticated():
        return

    if profile:
        for perm in get_perms_for_model(Profile):
            assign(perm.codename, user, profile)

    for perm in get_perms_for_model(User):
        assign(perm.codename, user, user)
