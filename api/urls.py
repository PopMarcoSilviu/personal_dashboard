from django.urls import path
from .views import UserRecordView, PersonalDashboardView

app_name = 'api'
urlpatterns = [
    path('user/', UserRecordView.as_view(), name='users'),
    path('pd/', PersonalDashboardView.as_view(), name='pd'),
]