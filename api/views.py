
import urllib.parse

from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponse, JsonResponse

from api.forms import PersonalDashboardForm, TaskForm, DrawingForm, NoteForm
from api.models import PersonalDashboard, Task, Drawing, Note


def errors_as_string(form):
    data = ''
    for item in form.errors.as_data().items():
        data += item[0] + ' ' + item[1][0].message
        data += ' '


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return JsonResponse(data={'id': user.id}, status=200)
        else:
            return HttpResponse(status=404, content=form.errors.as_data())


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return HttpResponse(status=200)
    return HttpResponse(status=404)


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=404, content=errors_as_string(form))


@login_required
def user_pd_view(request):
    if request.method == 'GET':
        try:
            if request.GET.get('get_all') == 'True':
                data = PersonalDashboard.objects.all().filter(user=request.user)
            else:
                data = PersonalDashboard.objects.all().filter(user=request.user, name=request.GET.get('name'))
            return JsonResponse(data=list(data.values()), safe=False, status=200)
        except TypeError as e:
            return HttpResponse(status=404)

    elif request.method == 'POST':
        form = PersonalDashboardForm(data=request.POST)
        form.user = request.user

        data = ''
        for item in form.errors.as_data().items():
            data += item[0] + ' ' + item[1][0].message
            data += ' '
        if form.is_valid():
            instance = form.save()
            return JsonResponse(data={'id': instance.id}, status=201)
        else:
            return HttpResponse(status=404, content=data)


def user_task_view(request):
    if request.method == 'POST':
        form = TaskForm(data=request.POST)

        if form.is_valid():
            instance = form.save()
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=404, content=errors_as_string(form))
    elif request.method == 'GET':
        try:
            data = urllib.parse.parse_qs(request.body.decode('utf-8'))
            data = Task.objects.all().filter(name=data['name'][0], pd=data['pd'][0])
            return JsonResponse(data=list(data.values()), safe=False, status=200)
        except TypeError:
            return HttpResponse(status=404)


def user_drawing_view(request):
    if request.method == 'POST':
        form = DrawingForm(data=request.POST)

        if form.is_valid():
            instance = form.save()
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=404, content=errors_as_string(form))
    elif request.method == 'GET':
        try:
            data = urllib.parse.parse_qs(request.body.decode('utf-8'))
            data = Drawing.objects.all().filter(pd=data['pd'][0])
            return JsonResponse(data=list(data.values()), safe=False, status=200)
        except TypeError:
            return HttpResponse(status=404)


def user_note_view(request):
    if request.method == 'POST':
        form = NoteForm(data=request.POST)

        if form.is_valid():
            instance = form.save()
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=404, content=errors_as_string(form))
    elif request.method == 'GET':
        try:
            data = urllib.parse.parse_qs(request.body.decode('utf-8'))
            data = Note.objects.all().filter(name=data['name'][0], pd=data['pd'][0])
            return JsonResponse(data=list(data.values()), safe=False, status=200)
        except TypeError:
            return HttpResponse(status=404)
