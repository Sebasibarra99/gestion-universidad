from django.contrib import admin
from gestionAcademico.models import Carrera, Curso, Estudiante, Matricula
# Register your models here.

class carreraAdmin(admin.ModelAdmin):
    list_display = ('codigo','nombre','duracion')
    list_filter = ('codigo','nombre')
    search_fields = ('codigo','nombre','duracion',)

class CursoAdmin(admin.ModelAdmin):
    list_display = ('codigo','nombre','creditos','docente')
    list_filter = ('docente','creditos')
    search_fields = ('codigo','nombre','docente',)


class matriculaAdmin(admin.ModelAdmin):
    list_display = ('id','estudiante','fechaMatricula')
    list_filter = ('id','estudiante','fechaMatricula')
    search_fields = ('id','estudiante',)

class estudianteAdmin(admin.ModelAdmin):
    list_display = ('documento','primerApellido','segundoApellido','nombres','fechaNacimiento','sexo','carrera','vigencia')
    list_filter = ('primerApellido','carrera')
    search_fields = ('documento','primerApellido','segundoApellido','nombres',)



admin.site.register(Matricula,matriculaAdmin)
admin.site.register(Estudiante,estudianteAdmin)
admin.site.register(Carrera,carreraAdmin)
admin.site.register(Curso,CursoAdmin)


 



