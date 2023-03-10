from vehicle import models as vehicle_models

class VehicleHandler:

    @classmethod
    def get_all_vehicles(cls):
        return vehicle_models.Vehicle.objects.all()

    @classmethod
    def get_vehicle_by_id(cls, vehicle_id):
        try:
            vehicle = vehicle_models.Vehicle.objects.get(id=vehicle_id)
            return vehicle
        except vehicle_models.Vehicle.DoesNotExist:
            return None

    @classmethod
    def delete_vehicle(cls, vehicle):
        vehicle.delete()