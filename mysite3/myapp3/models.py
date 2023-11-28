from django.db import models
from django.utils import timezone

class ContactList(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date_joined = models.DateField(null=True, blank=True)
    date_expired = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

    def can_delete(self):
        if self.date_joined and self.date_expired:
            one_year_from_joined = self.date_joined + timezone.timedelta(days=365)
            return self.date_expired <= one_year_from_joined
        return True



