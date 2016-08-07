"""SecretSanta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
#log_in, index, register, log_out, private_office, private_office_change, santa_for, \
from santa_app.views import santa_for, IndexView,LoginView, PrivateOffice, PrivateOfficeHhange, LogoutView, RegisterView, SecretButton

admin.autodiscover()

urlpatterns = [
    url(r'^$', IndexView.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', LoginView.as_view()),
    url(r'^logout/$', LogoutView.as_view()),
    url(r'^register/$', RegisterView.as_view()),
    url(r'^private_office/$', PrivateOffice.as_view()),
    url(r'^private_office_change/$', PrivateOfficeHhange.as_view(), name='private_offive_change'),
    url(r'^santa_for/$', santa_for.as_view()),
    url(r'^secret_button/$', SecretButton.as_view())
]
