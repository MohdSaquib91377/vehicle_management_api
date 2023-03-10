from rest_framework import serializers
from vehicle import models as vehicle_models

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = vehicle_models.Vehicle
        fields = "__all__"