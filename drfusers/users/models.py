from django.db import models
import bcrypt
import uuid
from django.contrib.auth.hashers import make_password


class Accounts(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False,
                          unique=True, primary_key=True)
    phone = models.CharField(max_length=12, null=False,
                             blank=False, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=300, null=False, blank=False)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    # username = models.CharField(max_length=120)

    def save(self, *args, **kwargs):
        hashed = make_password(self.password)
        self.password = hashed

        super(Accounts, self).save(*args, **kwargs)
