from rest_framework.response import Response 
from rest_framework.views import APIView
from account import service as account_service

class RegisterView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            status, data = account_service.AccountService.validate_register_payload(request.data)

        except Exception as e:
            status, data = 400, f"{e}"
        
        finally:
            return Response({"status": status, "data": data},status=status)