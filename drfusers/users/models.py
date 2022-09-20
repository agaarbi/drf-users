from django.db import models
import bcrypt
import uuid


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
        password = str(self.password)
        password = password.encode('utf-8')
        hashed = bcrypt.hashpw(password, bcrypt.gensalt())
        self.password = hashed

        # Checking
        # print(self.password)
        # if bcrypt.checkpw(password, hashed):
        #     print("match")
        # else:
        #     print("does not match")

        super(Accounts, self).save(*args, **kwargs)
