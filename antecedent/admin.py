from django.contrib import admin
from antecedent.models import Personne
from antecedent.models import CategorieCrime
from antecedent.models import Antecedent

# Register your models here.
admin.site.register(Personne)
admin.site.register(CategorieCrime)
admin.site.register(Antecedent)

