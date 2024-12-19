from django.core.mail import send_mail
from django.utils import timezone
from django.conf import settings
from goals.models import Goal
from django_cron import CronJobBase, Schedule


# Reminder email for upcoming fitness_project.core.goals
def send_goal_reminder(user, goal):
    subject = "Goal Reminder: Upcoming Deadline!"
    message = f"Hi {user.username},\n\nDon't forget to achieve your goal: {goal.title}"
    send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email])

# Send notifications on goal completion
def notify_goal_completion(user, goal):
    subject = "Congratulations! You've Achieved Your Goal"
    message = f"Hi {user.username},\n\nGreat job on achieving your goal: {goal.title}"
    send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email])

# Cron Job for sending reminders
class GoalReminderCronJob(CronJobBase):
    RUN_AT_TIMES = ['09:00']
    schedule = Schedule(run_at_times=RUN_AT_TIMES)
    code = 'fitness_project.core.workouts.goal_reminder_cron'  # Unique cron job code

    def do(self):
        today = timezone.now().date()
        goals = Goal.objects.filter(deadline__gte=today)
        for goal in goals:
            send_goal_reminder(goal.user, goal)
