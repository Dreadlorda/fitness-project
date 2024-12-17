
from .models import Badge

def user_badges(request):
    if request.user.is_authenticated:
        return {'badges': Badge.objects.filter(user=request.user)}
    return {}
