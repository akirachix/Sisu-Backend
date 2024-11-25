from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
class EmailBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        UserModel = get_user_model()
        print(f"$$$$$$$$$$$$$$$$$$$$$${email}%%%%%%%%%%%%%{password}%%%%")
        try:
            user = UserModel.objects.get(email=email)
            if user.check_password(password):
                return user
        except UserModel.DoesNotExist:
            return None