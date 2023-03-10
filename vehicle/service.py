from vehicle.api import serializers as vehicle_serializers
from vehicle import query as vehicle_query

class VehicleService:

    @staticmethod
    def validate_post_request(payload):
        serializer = vehicle_serializers.VehicleSerializer(data = payload)
        if serializer.is_valid():
            serializer.save()
            status, data = 200, "vehicle created successfully"

        else:
            status, data = 400, serializer.errors
        
        return status, data
    
    @staticmethod
    def validate_patch_request(payload, vehicle_id):
        vehicle = vehicle_query.VehicleHandler.get_vehicle_by_id(vehicle_id)
        if vehicle is None:
            return 400, 'vehicle not found'
        serializer = vehicle_serializers.VehicleSerializer(vehicle, data = payload, partial = True)
        if serializer.is_valid():
            serializer.save()
            return 200, 'Vehicle updated successfully'
        
        return 400, serializer.errors

    @staticmethod
    def list_vehicles():
        vehicles = vehicle_query.VehicleHandler.get_all_vehicles()
        serializer = vehicle_serializers.VehicleSerializer(vehicles, many=True)
        return 200, serializer.data
    
    @staticmethod
    def delete_existing_vehicle(vehicle_id):
        vehicle = vehicle_query.VehicleHandler.get_vehicle_by_id(vehicle_id)
        if vehicle is None:
            return 400, 'vehicle not found'
        
        vehicle_query.VehicleHandler.delete_vehicle(vehicle)
        return 200, 'Vehicle deleted successfully'

    @staticmethod
    def show_vehicle(vehicle_id):
        vehicle = vehicle_query.VehicleHandler.get_vehicle_by_id(vehicle_id)
        if vehicle is None:
            return 400, 'vehicle not found'
        
        serializer = vehicle_serializers.VehicleSerializer(vehicle, many=False)
        return 200, serializer.data