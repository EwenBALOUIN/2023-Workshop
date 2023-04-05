from django.db import models

class Action(models.Model):

    class ActionType(models.TextChoices):
        REMINDER = 'Rappel',
        CALL = 'Appel',
        EMAIL = 'Email',
        MEETING = 'Rendez-vous',
        VISIT = 'Visite',
        SALE = 'Vente',
        OTHER = 'Autre',
    
    action_type = models.CharField(
        max_length=30,
        choices=ActionType.choices,
        default=ActionType.OTHER,
    )

    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    scheduled_at = models.DateTimeField()
    done_at = models.DateTimeField(null=True, blank=True)
    customer = models.ForeignKey('Customer', on_delete=models.PROTECT, null=True, blank=True, related_name='action')

    def __str__(self):
        return self.action_type + ': ' + self.description