from django.utils.deprecation import MiddlewareMixin
from datetime import datetime
from task_board.settings import INACTIVITY_TIME
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib import messages


class AutoLogout(MiddlewareMixin):

    # def process_request(self, request):
    #     session_count = 0
    #     if request.user.is_authenticated:
    #         session_count = request.session.get('session_count')
    #         if request.method == 'GET':
    #             session_count += 1
    #         if not request.user.is_superuser:
    #             request.session.set_expiry(60*60)
    #     request.session.update({'session_count': session_count})

    def process_request(self, request):
        if request.user.is_authenticated and not request.user.is_superuser:
            time_now = datetime.now()
            last_activity = request.session.get('last_activity', time_now.isoformat())
            inactivity = time_now - datetime.fromisoformat(last_activity)
            if inactivity.seconds > INACTIVITY_TIME:
                logout(request)
                return HttpResponseRedirect(reverse_lazy('login'))
            request.session['last_activity'] = time_now.isoformat()


class ActionUser(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated and not request.user.is_superuser and request.method == 'GET':
            action = request.session.get('action', 0)
            action += 1
            request.session['action'] = action
            messages.info(request, f'{action}')
