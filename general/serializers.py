from rest_framework import serializers
from django.contrib.auth import get_user_model
from users.models import Country

User = get_user_model()

class ProfileEditConstituentSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["profile_picture"]


class CountryCustomisedForEmma(serializers.ModelSerializer):
    class Meta:
        model=Country
        fields=['id','name']

