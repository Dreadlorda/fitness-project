
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

class RoleRequiredMixin(UserPassesTestMixin):
    role = None  # Define 'admin', 'staff', or 'user' in views

    def test_func(self):
        if self.role == 'admin':
            return self.request.user.is_superuser
        elif self.role == 'staff':
            return self.request.user.is_staff
        elif self.role == 'user':
            return self.request.user.is_authenticated and not self.request.user.is_staff
        return False

class AuthRequiredMixin(LoginRequiredMixin):
    login_url = '/login/'  # Redirect to login page if not authenticated
    redirect_field_name = None
