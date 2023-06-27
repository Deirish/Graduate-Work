from django.utils.deprecation import MiddlewareMixin
from datetime import datetime
from task_board.settings import INACTIVITY_TIME
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib import messages


class AutoLogout(MiddlewareMixin):

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
        if request.user.is_authenticated and not request.user.is_superuser and request.methog == 'GET':
            action = request.session.get('action', 0)
            action += 1
            request.session['action'] = action
            messages.info(request, f'{action}')
