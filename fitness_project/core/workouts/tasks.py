from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone
from fitness_project.core.workouts.models import Goal
from django.conf import settings



@shared_task
def send_goal_reminder():
    today = timezone.now().date()
    goals = Goal.objects.filter(deadline=today)
    for goal in goals:
        subject = "Goal Reminder: Deadline Today!"
        message = f"Don't forget to achieve your goal: {goal.goal_type}. Target completion date: {goal.deadline}."
        recipient_email = goal.user.email
        send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient_email])

@shared_task
def notify_milestone_completion(user_email, milestone_name):
    subject = "Milestone Achieved!"
    message = f"Congratulations! You've achieved the milestone: {milestone_name}."
    send_mail(subject, message, settings.EMAIL_HOST_USER, [user_email])