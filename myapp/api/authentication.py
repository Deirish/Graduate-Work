from rest_framework.authentication import TokenAuthentication
from django.utils import timezone
from rest_framework import exceptions
from task_board import settings


class TokenExpiredAuthentication(TokenAuthentication):

    def authenticate(self, request):
        authenticate = super().authenticate(request)
        if authenticate:
            user, token = authenticate
        else:
            return authenticate
        if not user.is_superuser:
            if (timezone.now() - token.created).seconds > settings.TIME_TOKEN:
                token.delete()
                message = "Your token is not working! Create a new one."
                raise exceptions.AuthenticationFailed(message)
            elif (timezone.now() - token.created).seconds <= settings.TIME_TOKEN:
                token.created = timezone.now()
                token.save()
        return user, token

