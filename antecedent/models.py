from django.db import models

# Create your models here.

class Personne(models.Model):
    nom = models.CharField(max_length=256,null=True)
    prenom = models.CharField(max_length=256, null=True)
    date_naissance = models.DateField(max_length=256,null=True)
    lieu_naissance = models.CharField(max_length=256, null=True)
    lieu_de_residence = models.CharField(max_length=256,null=True)
    photo = models.ImageField(upload_to='media/images/', null=True, blank=True)

    def __str__(self):
        return '{} {}'.format(self.nom, self.prenom)

class CategorieCrime(models.Model):
    nom = models.CharField(max_length=256, null=True)

    def __str__(self):
        return '{}'.format(self.nom)


class Antecedent(models.Model):
    personne = models.ForeignKey(Personne, on_delete=models.CASCADE, default=1,null=True)
    categories = models.ForeignKey(CategorieCrime, on_delete=models.DO_NOTHING, default=1,null=True)
    description = models.TextField(null=True)
    date_des_faits = models.DateTimeField(null=True)

    def __str__(self):
        return '{} {} {} {}'.format(self.personne,self.description,self.categories,self.date_des_faits)



