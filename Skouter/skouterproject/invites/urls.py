from django.urls import path
from .views import CreateInviteView, RespondInviteView

urlpatterns = [

    path('', CreateInviteView.as_view()),
    path('<int:pk>/', RespondInviteView.as_view()),
]