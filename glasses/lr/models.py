from django.db import models

class Person(models.Model):
    GENDER_CHOICES = [
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other"),
    ]
    username = models.CharField(max_length=150)
    fullname = models.CharField(max_length=150, default="")
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=8)
    confirmpassword = models.CharField(max_length=8)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default="")
    otp = models.CharField(max_length=4, null=True, blank=True)
    country = models.CharField(max_length=10, default="")

    def __str__(self):
        return f"{self.username} - {self.fullname} - {self.email} - {self.phone} - {self.gender} - {self.country}"


class GenderChoices(models.IntegerChoices):
    MALE = 1, "MALE"
    FEMALE = 2, "FEMALE"
