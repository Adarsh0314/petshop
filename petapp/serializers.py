from .models import pet_tbl
from rest_framework import serializers


class petform(serializers.ModelSerializer):
    class Meta:
        model =pet_tbl
        fields ='__all__'
