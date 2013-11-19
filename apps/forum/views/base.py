from datetime import datetime
from django.http import Http404, HttpResponse
from django.views.generic.base import View
from django.views.generic.edit import UpdateView

from braces.views import LoginRequiredMixin
from django_misaka.templatetags.markdown import markdown

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


class MarkdownView(View):
    def post(self, request, *args, **kwargs):
        content = request.POST.get('content')

        return HttpResponse(markdown(content))
