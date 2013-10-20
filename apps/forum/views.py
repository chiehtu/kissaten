from datetime import datetime
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.dates import ArchiveIndexView
from django.views.generic.edit import BaseCreateView, CreateView, UpdateView
from django.views.generic.list import ListView

from braces.views import LoginRequiredMixin

from forum.forms import TopicForm, ReplyForm, NodeForm
from forum.models import Topic, Reply, Node


class BaseEditView(UpdateView):
    def get_object(self):
        obj = super(BaseEditView, self).get_object()

        if not obj.author == self.request.user:
            raise Http404

        return obj

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.updated_on = datetime.now()

        return super(BaseEditView, self).form_valid(form)


class ForumIndexView(ArchiveIndexView):
    model = Topic
    date_field = 'last_reply_on'
    allow_empty = True
    paginate_by = 10
    template_name = 'forum/index.html'


class TopicCreateView(LoginRequiredMixin, CreateView):
    form_class = TopicForm
    template_name = 'forum/topic_create_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.author_ip = self.request.META['REMOTE_ADDR']

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


class NodeIndexView(ListView):
    model = Node
    paginate_by = 10


class NodeCreateView(LoginRequiredMixin, CreateView):
    form_class = NodeForm
    template_name = 'forum/node_create_form.html'


class NodeDetailView(SingleObjectMixin, ListView):
    paginate_by = 10
    template_name = 'forum/node_detail.html'

    def get(self, request, *args, **kwargs):
        name = kwargs['name_slug']
        self.object = get_object_or_404(Node, name=name)

        return super(NodeDetailView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(NodeDetailView, self).get_context_data(**kwargs)
        context['object'] = self.object

        return context

    def get_queryset(self):
        return self.object.topics.all()


class NodeEditView(LoginRequiredMixin, UpdateView):
    model = Node
    form_class = NodeForm
    template_name = 'forum/node_edit_form.html'

    def get(self, request, *args, **kwargs):
        if not self.request.user.is_staff:
            raise Http404

        return super(NodeEditView, self).get(request, *args, **kwargs)

    def get_object(self):
        name = self.kwargs['name_slug']
        self.object = get_object_or_404(Node, name=name)
        return self.object


