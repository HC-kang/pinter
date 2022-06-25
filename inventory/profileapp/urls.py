from django.urls import path

from profileapp.views import profileCreateView



app_name = "profileapp"

urlpatterns = [
    path('create/', profileCreateView.as_view(), name = 'create')
]
