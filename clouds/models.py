from django.db import models

class Servives(models.Model):
    service_name = models.CharField(max_length=30)
    service_type = models.CharField(max_length=30)
    services_supported = models.TextField()