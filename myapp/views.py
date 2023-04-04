from django.shortcuts import redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView
from myapp.forms import UserCreateForm, TaskCreateForm, TaskSearchForm
from myapp.models import Column

class SuperUserRequiredMixin(UserPassesTestMixin):

    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self):
        return redirect('home')

class HomeView(TemplateView):
    template_name = 'home.html'


class NewUserView(CreateView):
    form_class = UserCreateForm
    template_name = 'registration/registration.html'
    success_url = '/'

    def form_valid(self, form):
        valid = super().form_valid(form)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return valid


class TaskListView(LoginRequiredMixin, ListView):
    model = Column
    template_name = 'tasks.html'
    extra_context = {'form': TaskCreateForm, 'form1': TaskSearchForm}

    def get_queryset(self):
        if not self.request.user.is_superuser:
            queryset = Column.objects.filter(owner=self.request.user)
            return queryset
        queryset = Column.objects.all()
        return queryset


class TaskCreateView(CreateView):
    template_name = 'tasks.html'
    http_method_names = ['post']
    form_class = TaskCreateForm
    success_url = '/tasks'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.owner = self.request.user
        obj.save()
        return super().form_valid(form)


class TaskSearchView(LoginRequiredMixin, ListView):
    model = Column
    template_name = 'search_task.html'
    extra_context = {'form1': TaskSearchForm}

    def get_queryset(self):
        status = self.request.GET['status']
        if not self.request.user.is_superuser:
            queryset = Column.objects.filter(author=self.request.user, status=status)
            return queryset
        queryset = Column.objects.filter(status=status)
        return queryset






