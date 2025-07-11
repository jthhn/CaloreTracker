from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model


User = get_user_model()

class EmailAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        # try to get user by emial
        try: 
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            return None
        
        # check password
        if user.check_password(password):
            return user
        return None
        