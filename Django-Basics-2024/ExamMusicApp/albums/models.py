from django.core.validators import MinValueValidator
from django.db import models

from profiles.models import Profile


# Create your models here.
class Album(models.Model):
    MAX_LENGTH_ALBUM_NAME = 30
    MAX_LENGTH_ARTIST = 30
    MAX_LENGTH_GENRE = 30
    MIN_PRICE = 0.0

    # enum - (value,label)
    class Genre(models.TextChoices):
        POP_MUSIC = 'pop_music', 'Pop Music'
        JAZZ_MUSIC = 'jazz_music', 'Jazz Music'
        R_B_MUSIC = 'r&b_music', "R&B Music"
        ROCK_MUSIC = 'rock_music', "Rock Music"
        COUNTRY_MUSIC = 'country_music', "Country Music"
        DANCE_MUSIC = 'dance_music', "Dance Music"
        HIP_HOP_MUSIC = 'hip_hop_music', "Hip Hop Music"
        OTHER = 'other', "Other"

    album_name = models.CharField(
        max_length=MAX_LENGTH_ALBUM_NAME,
        unique=True,
        verbose_name='Album Name'
    )

    artist = models.CharField(
        max_length=MAX_LENGTH_ARTIST,
    )

    genre = models.CharField(
        max_length=MAX_LENGTH_GENRE,
        choices=Genre.choices,
    )
    description = models.TextField(
        blank=True,
        null=True
    )

    image_URL = models.URLField()

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
