from django.forms import ModelForm

from forum.models import Node, Topic, Reply


class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = ('node', 'title', 'content')


class ReplyForm(ModelForm):
    class Meta:
        model = Reply
        fields = ('content', )


class NodeForm(ModelForm):
    class Meta:
        model = Node
        fields = ('name', 'description', )
