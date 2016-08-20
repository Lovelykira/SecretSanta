from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.views import View
from django.views.generic import TemplateView, FormView, UpdateView
from random import choice
import random
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

from santa_app.models import MyUser
from santa_app.forms import LoginForm, RegistrationForm, PrivateOfficeChangeForm


class IndexView(TemplateView):
    template_name = 'index.html'


class LoginView(FormView):
    template_name = 'log_in.html'
    form_class = LoginForm

    def form_valid(self, form):
        login(self.request, form.get_user())
        return HttpResponseRedirect('/')


class LogoutView(View):
    def get(self, request):
        logout(self.request)
        return HttpResponseRedirect('/')


class RegisterView(FormView):
    form_class = RegistrationForm
    template_name = 'register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return HttpResponseRedirect('/')


class PrivateOffice(TemplateView, LoginRequiredMixin):
    template_name = 'private_office.html'
    redirect_field_name = '/login/'


class PrivateOfficeHhange(UpdateView, LoginRequiredMixin):
    model = MyUser
    form_class = PrivateOfficeChangeForm
    template_name = 'private_office_change.html'
    success_url = '/private_office'
    redirect_field_name = '/login/'

    def get_object(self, queryset=None):
        return self.request.user

    # def form_valid(self, form):
    #     form.save()
    #     return HttpResponseRedirect('/private_office')
    #
    # def get(self, request, *args, **kwargs):
    #     form = PrivateOfficeChangeForm(instance=request.user)
    #     if int(request.path.split('/')[2]) == request.user.pk:
    #         return render(request, 'private_office_change.html', context={'form': form})
    #     else:
    #         return HttpResponseRedirect('/')


class santa_for( TemplateView, LoginRequiredMixin):
    template_name = 'you_are_santa_for.html'
    redirect_field_name = '/login/'


@method_decorator(staff_member_required, name='dispatch')
class SecretButton(TemplateView):
    template_name = 'secret_button.html'

    def get_users(self, user, users, santas):
        if santas:
            return [u for u in users if u!=user and not u.is_taken and not u.santa_for]
        else:
            return [u for u in users if u != user and not u.is_taken]


    def post(self, request, *args, **kwargs):
        users = list(MyUser.objects.all())
        random.shuffle(users)
        for i in range(0, len(users)-1):
            users[i].santa_for = users[i+1]
            users[i].santa_for.is_taken = True
            users[i].save()
        users[-1].santa_for = users[0]
        users[0].santa_for.is_taken = True
        users[-1].save()

        # for user in users:
        #     if self.get_users(user, users, True) != []:
        #         user.santa_for = choice(self.get_users(user, users, True))
        #     else:
        #         user.santa_for = choice(self.get_users(user, users, False))
        #     user.santa_for.is_taken = True
        #     user.save()
        return HttpResponseRedirect('/santa_for/')


