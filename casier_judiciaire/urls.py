"""casier_judiciaire URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from antecedent import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='index'),
    path('ajout_personne', views.ajout_personne, name='ajout_personne'),
    path('liste_personne', views.liste_personne, name='liste_personne'),
    path('detail_personne/<str:id_personne>', views.detail_personne, name='detail_personne'),
    path('rechercher_personne', views.rechercher_personne, name='rechercher_personne'),
    path('ajout_antecedent/<str:id_personne>', views.ajout_antecedent, name='ajout_antecedent'),
    path('supprimer_antecedent/<str:id_antecedent>', views.supprimer_antecedent, name='supprimer_antecedent'),
    path('modifier_antecedent/<str:id_antecedent>', views.modifier_antecedent, name='modifier_antecedent'),
    path('liste_antecedent', views.liste_antecedent, name='liste_antecedent'),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
