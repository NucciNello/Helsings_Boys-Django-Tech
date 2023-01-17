from rest_framework import serializers
from .models import Profile, Alumnus

class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["id","first_name", "second_name", "last_name", "username", "email", "mobile", "facebook",
                  "twitter", "instagram", "dob", "cv"]