from rest_framework import serializers

from django.core.exceptions import ValidationError
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    GENDER_CHOICES = [
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other"),
    ]

    gender = serializers.ChoiceField(choices=GENDER_CHOICES)

    class Meta:
        model = Person
        fields = "__all__"

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")
        confirmpassword = data.get("confirmpassword")
        phone = data.get("phone")

        if Person.objects.filter(username=username).exists():
            raise ValidationError("Username already exists")
        if len(str(phone)) != 10:
            raise ValidationError("Phone number is not valid")
        if password != confirmpassword:
            raise ValidationError("Passwords do not match")

        return data

    def create(self, validated_data):
        return super().create(validated_data)
    

class Loginserializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = ("username", "password")

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")
        person_details = Person.objects.filter(
            username=username, password=password
        ).first()
        if not person_details:
            raise ValidationError("Invalid Username or Password")
        return data
