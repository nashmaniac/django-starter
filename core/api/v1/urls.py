from django.urls import path
from . import views
urlpatterns = [
    path('me', views.UserApiView.as_view(), name='user_me_api_view'),
]