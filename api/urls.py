from django.urls import path, re_path
from django.views.decorators.csrf import csrf_exempt

from api import views

app_name = 'api'
urlpatterns = [
    path('login/', csrf_exempt(views.login_view)),
    path('logout/', csrf_exempt(views.logout_view)),
    path('register/', csrf_exempt(views.register_view)),
    path('user-pd/', csrf_exempt(views.user_pd_view)),
    path('user-task/', csrf_exempt(views.user_task_view)),
    path('user-drawing/', csrf_exempt(views.user_drawing_view)),
    path('user-note/', csrf_exempt(views.user_note_view)),

]
