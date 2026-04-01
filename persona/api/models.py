from django.db import models

# Create your models here.

class Persona(models.Model):

    # Fields
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    # Metadata
    class Meta:
        ordering = ['id']

    # Methods