# from rest_framework.authentication import TokenAuthentication
# from django.utils import timezone
# from task_board import settings
# from rest_framework import exceptions
#
#
# class TokenExpiredAuthentication(TokenAuthentication):
#
#     def authenticate(self, request):
#         authenticate = super().authenticate(request)
#         if authenticate:
#             user, token = authenticate
#         else:
#             return authenticate
#         if not user.is_staff:
#             if (timezone.now() - token.created).seconds > settings.TIME_TOKEN:
#                 token.delete()
#                 raise exсeptions.AuthenticationFailed('Your token is not working! Create a new one.')
#             elif (timezone.now() - token.created).seconds <= settings.TIME_TOKEN:
#                 token.created = timezone.now()
#                 token.save()
#         return user, token

