from django.db import models

# Create your models here.

class Roles(models.Model):
    cod_rol = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre    

class Usuario(models.Model):
    rut = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    telefono = models.CharField(max_length=30)
    cod_rol = models.ForeignKey(Roles, on_delete=models.CASCADE) 

    def __str__(self):
        return self.nombre      
    
class Paciente(models.Model):
    rut = models.CharField(primary_key=True, max_length=20)
    nombre = models.CharField(max_length=30)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=30)
    contrasena = models.CharField(max_length=128)
    confirmar_contrasena = models.CharField(max_length=128)

    def __str__(self):
        return self.nombre 

class Consulta_medica(models.Model):
    cod_consulta = models.AutoField(primary_key=True)
    fecha = models.DateField(auto_now_add=True)
    hora = models.DateField(auto_now=True)
    rut_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    rut_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.cod_consulta)      
    
class Informe(models.Model):
    cod_informe = models.AutoField(primary_key=True)    
    cod_consulta = models.ForeignKey(Consulta_medica, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.cod_consulta)