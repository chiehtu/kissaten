from django.shortcuts import get_object_or_404
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from braces.views import LoginRequiredMixin, StaffuserRequiredMixin

from forum.forms import NodeForm
from forum.models import Node


class NodeIndexView(ListView):
    model = Node
    paginate_by = 10


class NodeCreateView(LoginRequiredMixin, StaffuserRequiredMixin, CreateView):
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


class NodeEditView(LoginRequiredMixin, StaffuserRequiredMixin, UpdateView):
    model = Node
    form_class = NodeForm
    template_name = 'forum/node_edit_form.html'

    def get_object(self):
        name = self.kwargs['name_slug']
        self.object = get_object_or_404(Node, name=name)
        return self.object


