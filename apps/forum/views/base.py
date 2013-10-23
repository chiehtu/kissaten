from datetime import datetime
from django.http import Http404
from django.views.generic.edit import UpdateView


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
