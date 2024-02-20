import re

from django.core.exceptions import ValidationError


def validate_names(value):
    pattern = r'^[a-zA-Z0-9_]+$'
    # Check if the value matches the pattern
    if not re.match(pattern, value):
        raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")
