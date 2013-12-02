from datetime import datetime
from django.views.generic.edit import BaseCreateView

from braces.views import LoginRequiredMixin

from .base import BaseEditView
from forum.forms import ReplyForm
from forum.models import Topic, Reply


class ReplyCreateView(LoginRequiredMixin, BaseCreateView):
    model = Topic
    form_class = ReplyForm
    http_method_names = ['post', 'put']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.author_ip = self.request.META['REMOTE_ADDR']

        self.object.topic = self.get_object()
        self.object.topic.num_replies += 1
        self.object.topic.last_reply_on = datetime.now()
        self.object.topic.save()

        return super(ReplyCreateView, self).form_valid(form)

    def get_success_url(self):
        return self.object.topic.get_absolute_url()


class ReplyEditView(LoginRequiredMixin, BaseEditView):
    model = Reply
    form_class = ReplyForm
    template_name = 'forum/reply_edit_form.html'

    def get_success_url(self):
        return self.object.topic.get_absolute_url()
