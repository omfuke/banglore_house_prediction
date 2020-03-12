from rest_framework import serializers
from .models import HouseModel


class HouseSerializers(serializers.ModelSerializer):

    class Meta:

        model = HouseModel
        fields = '__all__'