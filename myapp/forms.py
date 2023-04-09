from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.db.models import F
from myapp.models import Column, TASK
from django.core.exceptions import ValidationError



class UserCreateForm(UserCreationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput)
    email = forms.EmailField(widget=forms.EmailInput)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError('Email is already registered')
        return email


class TaskCreateForm(forms.ModelForm):
    text = forms.TextInput()

    class Meta:
        model = Column
        fields = ['text']


class TaskSearchForm(forms.ModelForm):
    status = forms.ChoiceField(choices=TASK, label='status_task')

    class Meta:
        model = Column
        fields = ['status']


class TaskChangeForm(forms.ModelForm):
    executor = forms.ModelChoiceField(queryset=User.objects.all(), label='Executor', blank=True, required=False)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(TaskChangeForm, self).__init__(*args, **kwargs)
        if user and user.is_authenticated and not user.is_superuser:
            self.fields['executor'].queryset = User.objects.filter(id=user.id)

    class Meta:
        model = Column
        fields = ['text', 'executor']


class TaskUpForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(TaskUpForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Column
        fields = ()

    def save(self, commit=True):
        response = super().save(commit=False)
        user = self.user
        if user and user.is_authenticated and (not user.is_superuser and response.owner == response.executor and
                 response.status < 4 or user.is_superuser and response.status == 4):
            response.status = F('status') + 1
        if commit:
            response.save()
            self.save_m2m()
            return response


class TaskDownForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(TaskDownForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Column
        fields = ()

    def save(self, commit=True):
        response = super().save(commit=False)
        user = self.user
        if user and user.is_authenticated and \
                (not user.is_superuser and response.owner == response.executor and
                 response.status > 1 and response.status != 5 or
                 user.is_superuser and response.status == 5):
            response.status = F('status') - 1
        if commit:
            response.save()
            self.save_m2m()
        return response










