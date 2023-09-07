from django.views.generic import TemplateView


# Create your views here.

class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class ChangePasswordView(TemplateView):
    template_name = 'registration/password_change_done.html'
