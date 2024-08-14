from django.contrib.auth.views import LoginView
from django.shortcuts import render

class CustomLoginView(LoginView):
    template_name = 'layout/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return '/dashboard/'
    def form_invalid(self, form):
        return super().form_invalid(form)
    
def contact(request):
    return render(request, 'layout/contact.html')

