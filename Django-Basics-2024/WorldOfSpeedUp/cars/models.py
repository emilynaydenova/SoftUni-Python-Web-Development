from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from cars.validators import validate_year, validate_secure_url
from profiles.models import Profile


class Car(models.Model):
    MAX_LENGTH_TYPE = 10

    MAX_LENGTH_MODEL = 15
    MIN_LENGTH_MODEL = 1

    MIN_PRICE = 1.0

    class CarTypes(models.TextChoices):
        RALLY = 'rally', 'Rally'
        OPEN_WHEEL = 'open_wheel', 'Open-wheel'
        KART = 'kart', 'Kart'
        DRAG = 'drag', 'Drag'
        OTHER = 'other', "Other"

    type = models.CharField(
        max_length=MAX_LENGTH_TYPE,
        choices=CarTypes.choices,
    )

    model = models.CharField(
        max_length=MAX_LENGTH_MODEL,
        validators=(
            MinLengthValidator(MIN_LENGTH_MODEL),
        )
    )

    year = models.PositiveIntegerField(
        validators=(
            validate_year,
        )
    )
    # A placeholder: "https://..." in the form
    imageURL = models.URLField(
        unique=True,
        error_messages={
            'unique': "This image URL is already in use! Provide a new one.",
        },
        validators=(
            validate_secure_url,
        )
    )

    price = models.FloatField(
        validators=[
            MinValueValidator(MIN_PRICE),
        ]
    )

    # hidden in the form
    owner = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE
    )
