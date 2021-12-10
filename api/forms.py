from django.forms import ModelForm

from api.models import PersonalDashboard, Task, Note, Drawing


class PersonalDashboardForm(ModelForm):
    class Meta:
        model = PersonalDashboard
        fields = ['type_of_pd', 'user', 'name']


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'date_to_complete', 'pd']


class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'msg', 'pd']


class DrawingForm(ModelForm):
    class Meta:
        model = Drawing
        fields = ['drawing', 'pd']
