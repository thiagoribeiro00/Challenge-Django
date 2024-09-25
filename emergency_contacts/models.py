from django.db import models
from django.core.exceptions import ValidationError

def validate_phone(value):
    if not value.isdigit() or len(value) != 10:  # Validar se é um número com 10 dígitos
        raise ValidationError("Phone number must be a 10-digit number.")

class Contact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=10, validators=[validate_phone])

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.phone_number})"
