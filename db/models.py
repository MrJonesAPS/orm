import sys


try:
    from django.db import models
except Exception:
    print('Exception: Django Not Found, please install it with "pip install django".')
    sys.exit()


# Sample User model


# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=255)
    long = models.DecimalField(max_digits=23, decimal_places=20)
    lat = models.DecimalField(max_digits=23, decimal_places=20)
    # owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
