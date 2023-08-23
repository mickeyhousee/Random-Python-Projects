#!/usr/bin/python3
#MADE BY: mickeyhousee

from plyer import notification

notification_title = "This is a test title"
notification_message = "This is a test message!"

notification.notify(
    title=notification_title,
    message=notification_message,
    app_icon=None,
    timeout=10,
    toast=False
)