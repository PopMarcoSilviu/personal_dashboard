from django.contrib import admin

# Register your models here.
from api.models import PersonalDashboard, Note, Task, Drawing

admin.site.register(PersonalDashboard)
admin.site.register(Note)
admin.site.register(Drawing)
admin.site.register(Task)
