from .models import Notification

def notifications_context(request):
    if request.user.is_authenticated:
        notifications = Notification.objects.filter(
            user=request.user,
            is_read=False
        ).order_by("-created_at")

        return {
            "notifications": notifications,
            "unread_count": notifications.count()
        }

    return {}