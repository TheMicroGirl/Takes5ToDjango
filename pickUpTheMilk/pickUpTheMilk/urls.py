"""pickUpTheMilk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import include
from MILK import views
from django.conf import settings
from django.conf.urls.static import static
from MILK.views import MyRegistrationView

# Include this custom form as it has different help text for username field.
from MILK.forms import CustomRegistration

urlpatterns = [
    url(r'^', include('MILK.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/register/',
        MyRegistrationView.as_view(template_name='registration/registration_form.html',
        form_class=CustomRegistration), name='registration_register'),
    url(r'^accounts/', include('registration.backends.simple.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
