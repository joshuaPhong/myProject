from django.urls import path
from .views import HomePageView, ChangePasswordView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('registration/password_change_done', ChangePasswordView.as_view(),
         name='done')

]
