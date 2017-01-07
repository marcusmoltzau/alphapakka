"""alphapakka URL Configuration

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
import alphapakka.views

urlpatterns = [
    url(r'promille/$', alphapakka.views.promille),
    url(r'^$', alphapakka.views.VelkommstVIEW),
    url(r'klokka/$', alphapakka.views.KlokkeVIEW),
    url(r'promille/klokka/pluss/(\d{1,2})/$', alphapakka.views.KlokkeVIEW_Fremover),
    url(r'dato/', alphapakka.views.KlokkeVIEW),
    url(r'^admin/', admin.site.urls),
    url(r'^kalsiumkarbonat/$ ', alphapakka.views.Pers_FAVORITT_View),
    url(r'^videre/$', alphapakka.views.tidssjefen),
]




