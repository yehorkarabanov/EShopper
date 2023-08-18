from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, View
from .models import UserAccount
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import redirect, HttpResponse
from django.http import JsonResponse
from .forms import ExtendedUserCreationForm


@method_decorator(login_required, name='dispatch')
class AccountDetailView(DetailView):
    model = UserAccount
    template_name = 'account/account.html'
    context_object_name = 'account'

    def get_object(self, queryset=None):
        return self.request.user.useraccount


@method_decorator(login_required, name='dispatch')
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('shop:home')


class LoginView(View):
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'status': 'success', 'username': user.username})
        return JsonResponse({'status': 'failed'})


class UserRegisterView(View):
    def post(self, request):
        form = ExtendedUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            account = UserAccount.objects.create(user=user)
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return JsonResponse({'status': 'success', 'username': user.username})
        return JsonResponse({'status': 'failed', 'errors': form.errors})
