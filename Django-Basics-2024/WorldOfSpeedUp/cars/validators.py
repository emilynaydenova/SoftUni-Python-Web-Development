from django.core.exceptions import ValidationError


def validate_year(value):
    if value < 1999 or value > 2030:
        raise ValidationError("Year must be between 1999 and 2030!")


def validate_secure_url(value):
    url = value.strip().lower()
    if not url.startswith("https://"):
        raise ValidationError("Not secure URL.")
