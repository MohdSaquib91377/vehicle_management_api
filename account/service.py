from account.api import serializers as account_serializer



class AccountService:
    @staticmethod
    def validate_register_payload(payload):
        serilizer = account_serializer.RegisterSerializer(data = payload)
        if serilizer.is_valid():
            serilizer.save(is_customer = True)
            return 200, f'Registration successful'
        return 400, serilizer.errors