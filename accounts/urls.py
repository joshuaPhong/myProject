from django.urls import path
from .views import SignUpView, ChangePasswordView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('registration/password_change_done', ChangePasswordView.as_view(),
         name='done')

]
