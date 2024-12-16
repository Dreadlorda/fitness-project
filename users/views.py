
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect

# Check if the user is a staff member
def is_staff(user):
    return user.is_staff

# Check if the user is a superuser
def is_superuser(user):
    return user.is_superuser

@login_required
@user_passes_test(is_staff, login_url="/login/", redirect_field_name=None)
def staff_dashboard(request):
    # Staff members' dashboard
    return render(request, "users/staff_dashboard.html")

@login_required
@user_passes_test(is_superuser, login_url="/login/", redirect_field_name=None)
def admin_dashboard(request):
    # Superusers' dashboard
    return render(request, "users/admin_dashboard.html")

@login_required
def user_dashboard(request):
    # Regular user dashboard
    if request.user.is_staff or request.user.is_superuser:
        return redirect("/admin_dashboard/" if request.user.is_superuser else "/staff_dashboard/")
    return render(request, "users/user_dashboard.html")

from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .forms import LoginForm

class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    authentication_form = LoginForm

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')  # Redirect to login page after logout

from django.views.generic import TemplateView
from .mixins import RoleRequiredMixin

class AdminDashboardView(RoleRequiredMixin, TemplateView):
    template_name = 'users/admin_dashboard.html'
    role = 'admin'

class StaffDashboardView(RoleRequiredMixin, TemplateView):
    template_name = 'users/staff_dashboard.html'
    role = 'staff'

class UserDashboardView(RoleRequiredMixin, TemplateView):
    template_name = 'users/user_dashboard.html'
    role = 'user'

import asyncio
from django.http import JsonResponse
from django.views import View

class AsyncDemoView(View):
    async def get(self, request, *args, **kwargs):
        await asyncio.sleep(2)  # Simulate a delay (e.g., database or API call)
        return JsonResponse({"status": "success", "message": "Async response!"})
