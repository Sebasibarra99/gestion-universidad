from django.db import models

# Create your models here.

class Carrera(models.Model):
    codigo = models.CharField(max_length=10,primary_key=True)
    nombre = models.CharField(max_length=50)
    duracion = models.PositiveSmallIntegerField(default=5)

    def __str__(self):
        return '{}'.format(self.nombre)


class Estudiante(models.Model):
    documento= models.CharField(max_length=35,primary_key=True)
    primerApellido= models.CharField(max_length=35)
    segundoApellido= models.CharField(max_length=35)
    nombres = models.CharField(max_length=35)
    fechaNacimiento = models.DateField()
    sexos = [('M','Masculino'),('F','Femenino')]
    sexo = models.CharField(max_length=1,choices=sexos,default='M')
    carrera = models.ForeignKey(Carrera,null=False,blank=False,on_delete=models.CASCADE)
    vigencia = models.BooleanField(default=True)

class Curso(models.Model):
    codigo = models.CharField(max_length=6,primary_key=True)
    nombre = models.CharField(max_length=30)
    creditos = models.PositiveSmallIntegerField()
    docente = models.CharField(max_length=100)

class Matricula(models.Model):
    id = models.AutoField(primary_key = True)
    estudiante = models.ForeignKey(Estudiante,null=False,blank=False,on_delete=models.CASCADE)
    fechaMatricula = models.DateTimeField(auto_now_add=True)
