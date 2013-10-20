from django.forms import ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Button, Layout, Submit
from crispy_forms.bootstrap import FormActions

from forum.models import Node, Topic, Reply


class TopicForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(TopicForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
            'node',
            'title',
            'content',
            FormActions(
                Submit('save', 'Save changes'),
                Button('cancel', 'Cancel')
            )
        )

    class Meta:
        model = Topic
        fields = ('node', 'title', 'content')


class ReplyForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ReplyForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
            'content',
            FormActions(
                Submit('save', 'Save changes'),
                Button('cancel', 'Cancel')
            )
        )

    class Meta:
        model = Reply
        fields = ('content', )


class NodeForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(NodeForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
            'name',
            'description',
            FormActions(
                Submit('save', 'Save changes'),
                Button('cancel', 'Cancel')
            )
        )

    class Meta:
        model = Node
        fields = ('name', 'description', )

