from datetime import datetime
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from braces.views import LoginRequiredMixin

from .base import BaseEditView
from forum.forms import TopicForm, ReplyForm
from forum.models import Topic


class ForumIndexView(ListView):
    model = Topic
    paginate_by = 10
    template_name = 'forum/index.html'


class TopicCreateView(LoginRequiredMixin, CreateView):
    form_class = TopicForm
    template_name = 'forum/topic_create_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.author_ip = self.request.META['REMOTE_ADDR']
        self.object.last_reply_on = datetime.now()

        return super(TopicCreateView, self).form_valid(form)


class TopicDetailView(SingleObjectMixin, ListView):
    paginate_by = 10
    template_name = 'forum/topic_detail.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Topic.objects.all())
        self.object.num_hits += 1
        self.object.save()
        return super(TopicDetailView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(TopicDetailView, self).get_context_data(**kwargs)

        if self.request.user.is_authenticated():
            context['form'] = ReplyForm()

        context['object'] = self.object

        return context

    def get_queryset(self):
        return self.object.replies.all()


class TopicEditView(LoginRequiredMixin, BaseEditView):
    model = Topic
    form_class = TopicForm
    template_name = 'forum/topic_edit_form.html'

