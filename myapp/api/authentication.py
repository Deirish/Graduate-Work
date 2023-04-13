from rest_framework.authentication import TokenAuthentication
from django.utils import timezone
from django.conf import settings


class TokenAuthenticationExpired(TokenAuthentication):

    def authenticate(self,request):
        authenticate = super().authenticate(request)
        if authenticate:
            user, token = authenticate
        else:
            return authenticate
        if not user.is_staff:
            if (timezone.now() - token.created).seconds > settings.TIME_TOKEN:
                token.delete()

