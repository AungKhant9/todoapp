from django.db import models

class user(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    in_active = models.BooleanField(default=True)

    def __str__(self):
        return self.user
