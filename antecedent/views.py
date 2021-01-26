from django.shortcuts import render,redirect
from antecedent.models import Personne
from antecedent.models import Antecedent
from antecedent.models import CategorieCrime

def home(request):
    return render(request,'index.html')

def ajout_personne(request):
    if request.method == 'POST':
        nom = request.POST.get('nom','')
        prenom = request.POST.get('prenom', '')
        date_naissance = request.POST.get('date_naissance', '')
        lieu_naissance = request.POST.get('lieu_naissance', '')
        lieu_de_residence = request.POST.get('lieu_de_residence', '')
        photo = request.FILES.get('photo', '')
        personnes = Personne()
        personnes.nom = nom
        personnes.prenom = prenom
        personnes.date_naissance = date_naissance
        personnes.lieu_naissance = lieu_naissance
        personnes.lieu_de_residence = lieu_de_residence
        personnes.photo = photo
        personnes.save()
        return redirect('rechercher_personne')
    return render(request,'ajout_personne.html')

def liste_personne(request):
    personnes = Personne.objects.filter()
    context = {"personnes": personnes}
    return render(request, "liste_personne.html", context)

def rechercher_personne(request):
    search = request.GET.get('Search')
    personnes = []
    print(search)
    if search == None:
        personnes = Personne.objects.all()
    else:
        personnes = Personne.objects.filter(nom__icontains=search)
    print(Personne)

    context = {'personnes': personnes}
    return render(request, 'rechercher_personne.html',context)

def detail_personne(request,id_personne):
    personne= Personne.objects.get(id=id_personne)
    antecedents = Antecedent.objects.filter(personne=personne)
    compte = {'personne': personne, 'antecedents': antecedents}
    return render(request, 'detail_personne.html', compte)

def ajout_antecedent(request,id_personne):
    personne = Personne.objects.get(id=id_personne)
    liste_categories = CategorieCrime.objects.all()
    if request.method == 'POST':
        categorie_id = request.POST.get('categorie_id', '')
        description = request.POST.get('description', '')
        date_des_faits = request.POST.get('date_des_faits', '')
        antecedent = Antecedent()
        categories = CategorieCrime.objects.get(id=categorie_id)
        antecedent.categories = categories
        antecedent.description = description
        antecedent.date_des_faits = date_des_faits
        antecedent.personne = personne
        antecedent.save()

        return redirect('detail_personne',personne.id)
    return render(request,'ajout_antecedent.html',locals())

def supprimer_antecedent(request,id_antecedent):
    antecedent = Antecedent.objects.get(id=id_antecedent)
    id_personne = antecedent.personne.id
    antecedent.delete()
    return redirect('detail_personne',id_personne)

def modifier_antecedent(request,id_antecedent):
    liste_categories = CategorieCrime.objects.all()
    antecedent = Antecedent.objects.get(id=id_antecedent)
    if request.method=='POST':
        categorie_id = request.POST.get('categorie_id', '')
        description = request.POST.get('description', '')
        date_des_faits = request.POST.get('date_des_faits', '')
        categories = CategorieCrime.objects.get(id=categorie_id)
        antecedent.categories = categories
        antecedent.description = description
        antecedent.date_des_faits = date_des_faits
        antecedent.save()
        return redirect('detail_personne',antecedent.personne.id)
    return render(request,'modifier_antecedent.html',locals())



def liste_antecedent(request):
    antecedents = Antecedent.objects.filter()
    context = {'antecedents':antecedents}
    return render(request, 'liste_antecedent.html',context)
