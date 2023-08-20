from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, View
from .models import UserAccount
from order.models import Order
from django.contrib.auth import logout, authenticate, login, update_session_auth_hash
from django.shortcuts import redirect, HttpResponse
from django.http import JsonResponse
from .forms import ExtendedUserCreationForm, ExtendedUserChangeForm, AccountUpdateForm
from django.contrib.auth.forms import PasswordChangeForm


@method_decorator(login_required, name='dispatch')
class AccountDetailView(DetailView):
    model = UserAccount
    template_name = 'account/account.html'
    context_object_name = 'account'

    def get_object(self, queryset=None):
        return self.request.user.account

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        orders = Order.objects.filter(email=self.request.user.email)
        context['orders'] = orders
        return context


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


@method_decorator(login_required, name='dispatch')
class PasswordChangeView(View):
    def post(self, request):
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return JsonResponse({'status': 'success'})
        return JsonResponse({'status': 'failed', 'errors': form.errors})


@method_decorator(login_required, name='dispatch')
class UserDataChange(View):
    def post(self, request):
        data = request.POST
        user_form = ExtendedUserChangeForm(instance=request.user, data=request.POST)
        account_form = AccountUpdateForm(instance=request.user.account, data=request.POST)
        if user_form.is_valid() and account_form.is_valid():
            user_form.save()
            account_form.save()
            return JsonResponse({'status': 'success'})
        return JsonResponse({'status': 'failed', 'errors': {**user_form.errors, **account_form.errors}})
