from django.db import models

class User(models.Model):

    class Status(models.TextChoices):
        NONE = 'aucun',
        LEAD = 'lead',
        LEAD_DEAD = 'lead mort',
        PROSPECT = 'prospect',
        PROSPECT_DEAD = 'prospect mort',
        CLIENT = 'client',

    status = models.CharField(
        max_length=30,
        choices=Status.choices,
        default=Status.NONE,
    )
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name
