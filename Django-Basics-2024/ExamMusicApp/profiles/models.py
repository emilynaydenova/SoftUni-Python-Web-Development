from django.core.validators import MinLengthValidator
from django.db import models

from validators import validate_names
# Create your models here.


class Profile(models.Model):
    MAX_LENGTH_USERNAME = 15
    MIN_LENGTH_USERNAME = 2

    username = models.CharField(
        max_length=MAX_LENGTH_USERNAME,
        validators=(
            MinLengthValidator(MIN_LENGTH_USERNAME),
            validate_names,
             )
        )

    email = models.EmailField()

    age = models.PositiveIntegerField(
        blank=True,
        null=True,
    )

