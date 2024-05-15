from django import template
from django.utils import timezone

register = template.Library()


@register.simple_tag
def due_date_class(due_date):
    """Returns a CSS class based on the task's due date proximity to the current date."""
    if due_date is None:
        print("No due date set")  # Debug message
        return ''  # Return an empty string if there's no due date

    # Calculate the difference in days between today and the due date
    today = timezone.localdate()
    delta = (due_date - today).days
    print(f"Due date: {due_date}, Today: {today}, Delta: {delta}")  # Debug message

    # Determine the appropriate class based on the delta
    if delta < 0:
        print("Date is in the past")  # Debug message
        return 'text-muted'  # Use muted text for past dates
    elif delta == 0:
        print("Date is today")  # Debug message
        return 'text-danger'  # Use danger text for today
    elif 1 <= delta <= 3:
        print("Date is within 3 days")  # Debug message
        return 'text-warning'  # Use warning text for upcoming dates within 3 days
    else:
        print("Date is more than 3 days away")  # Debug message
        return ''  # Default, no special class for dates more than 3 days away
