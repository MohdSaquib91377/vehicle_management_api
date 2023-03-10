from rest_framework.response import Response
from rest_framework.views import APIView
from vehicle import service as vehicle_service
from vehicle import permissions as vehicle_permissions
from rest_framework import permissions

class VehicleView(APIView):
    permission_classes = [vehicle_permissions.IsSuperAdminOrReadOnly]

    def post(self, request, *args, **kwargs):
        try:
            status, data = vehicle_service.VehicleService.validate_post_request(request.data)
            
        except Exception as e:
            status, data = 400, e

        finally:
            return Response({"sattus":status,"data":data}, status=status)
        
    def get(self, request, *args, **kwargs):
        try:
            status, data = vehicle_service.VehicleService.list_vehicles()
            
        except Exception as e:
            status, data = 400, e

        finally:
            return Response({"sattus":status,"data":data}, status=status)



class VehicleDetailsView(APIView):
    permission_classes = [vehicle_permissions.IsSuperAdminOrReadOnly | vehicle_permissions.IsAdmin]
    def get(self, request,vehicle_id,*args, **kwargs):
        try:
            status, data = vehicle_service.VehicleService.show_vehicle(vehicle_id)
            
        except Exception as e:
            status, data = 400, e

        finally:
            return Response({"sattus":status,"data":data}, status=status)

    def patch(self, request,vehicle_id,*args,**kwargs):
        try:
            status, data = vehicle_service.VehicleService.validate_patch_request(request.data,vehicle_id)
            
        except Exception as e:
            status, data = 400, e

        finally:
            return Response({"sattus":status,"data":data}, status=status)

    def delete(self, request,vehicle_id,*args,**kwargs):
        try:
            status, data = vehicle_service.VehicleService.delete_existing_vehicle(vehicle_id)
            
        except Exception as e:
            status, data = 400, e

        finally:
            return Response({"sattus":status,"data":data}, status=status)


                

