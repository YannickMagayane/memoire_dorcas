from django.db import models

# Create your models here.


type_day = (
    ('lundi','Lundi'),
    ('mardi','Mardi'),
    ('mercredi','Mercredi'),
    ('jeudi','Jeudi'),
    ('vendredi','Vendredi'),
    ('samedi','Samedi'),
    ('dimanche','Dimanche'),
)


type_promotion = (
    ('preparatoire','Preparatoire'),
    ('bac_1','Bac 1'),
    ('bac_2','Bac 2'),
    ('bac_3','Bac 3'),
    ('master_1','Master 1'),
    ('master_2','Master 2'),

)


class Departement(models.Model):
    departement = models.CharField(max_length=100,unique=True)
    filiere = models.CharField(max_length=100,unique=True,blank=True)
    promotion = models.CharField(max_length=50,choices=type_promotion,default='preparatoire')

    def __str__(self):
        return self.promotion +' ' + self.departement + ' filière ' + self.filiere

class Salles (models.Model):
    numero_salle = models.PositiveIntegerField(default=1)
    nom_salle = models.CharField(max_length=50,blank=True)
    promotion = models.CharField(max_length=50, unique= True)

    def __str__(self):
        return self.nom_salle


class Horaire (models.Model):
    jour = models.CharField(max_length=50,choices=type_day)
    heure_debut = models.TimeField()
    heure_fin = models.TimeField()
    cours = models.CharField(max_length=100)
    promotion = models.ForeignKey(Departement,on_delete=models.CASCADE)
    salles = models.ForeignKey(Salles,on_delete=models.CASCADE)
    date_creation = models.DateField()

    def __str__(self):
        return self.cours
