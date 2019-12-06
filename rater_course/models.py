from django.db import models


class RateCourse(models.Model):
    # in this model we are created three fields like: usd, uah and timestump.
    usd = models.FloatField(
        default=1.0,
        verbose_name='Dollar'
    )

    uah = models.FloatField(
        max_length=1000,
        blank=False,
        verbose_name='UAH'
    )

    timestamp = models.DateField(
        blank=False,
        auto_now=False
    )
