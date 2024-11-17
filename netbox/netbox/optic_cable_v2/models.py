from django.db import models

from django.utils.translation import gettext_lazy as _

class SplicePlate(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.name

class Coupler(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    splice_scheme = models.FileField(upload_to='coupler_schemes/', null=True, blank=True)

    def __str__(self):
        return self.name

class Fiber(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    cable = models.ForeignKey('Cable', on_delete=models.CASCADE, related_name='fibers')

    def __str__(self):
        return f"Fiber {self.name}"

class Module(models.Model):
    name = models.CharField(max_length=100)
    fiber_count = models.PositiveIntegerField()
    cable = models.ForeignKey('Cable', on_delete=models.CASCADE, related_name='modules')

    def __str__(self):
        return self.name

class Cable(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

