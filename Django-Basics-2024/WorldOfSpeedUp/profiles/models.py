from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from profiles.validators import validate_names


class Profile(models.Model):
    MAX_LENGTH_USERNAME = 15
    MIN_LENGTH_USERNAME = 3

    MIN_VALUE_AGE = 21

    MAX_LENGTH_PASSWORD = 20

    MAX_LENGTH_FIRSTNAME = 25
    MAX_LENGTH_LASTNAME = 25

    username = models.CharField(
        max_length=MAX_LENGTH_USERNAME,
        validators=(
            MinLengthValidator(
                MIN_LENGTH_USERNAME,
                "Username must be at least 3 chars long!"
            ),
            validate_names,
        )
    )

    email = models.EmailField()

    age = models.PositiveIntegerField(
        validators=(
            MinValueValidator(MIN_VALUE_AGE),
        ),
        help_text="Age requirement: 21 years and above.",
    )

    password = models.TextField(
        max_length=MAX_LENGTH_PASSWORD,
    )

    first_name = models.CharField(
        max_length=MAX_LENGTH_FIRSTNAME,
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        max_length=MAX_LENGTH_LASTNAME,
        blank=True,
        null=True,
    )

    profile_picture = models.URLField(
        blank=True,
        null=True,
    )
