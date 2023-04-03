from django.db import models

class Customer(models.Model):
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
    first_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    # company = models.ForeignKey('Company', on_delete=models.CASCADE, blank=True, null=True, related_name='customers')
    # company = models.ManyToManyField('Company', blank=True, related_name='customers')

    def __str__(self):
        return self.name + self.first_name