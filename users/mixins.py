
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

class RoleRequiredMixin(UserPassesTestMixin):
    role = None  # Define 'admin', 'staff', or 'user' in views

    def test_func(self):
        if not hasattr(self, 'request'):
            return False
        user = getattr(self.role, 'user', None)
        if user is None:
            return False
        if self.role == 'admin':
            return user.is_superuser
        elif self.role == 'staff':
            return user.is_staff
        elif self.role == 'user':
            return user.is_authenticated and not user.is_anonymous
        return False

class AuthRequiredMixin(LoginRequiredMixin):
    login_url = '/login/'  # Redirect to login page if not authenticated
    redirect_field_name = None
