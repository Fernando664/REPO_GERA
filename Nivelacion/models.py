from django.db import models

class RegistroMateria(models.Model):
    nombre_materia = models.CharField(max_length=100)
    profesor = models.CharField(max_length=100, blank=True)
    comentario = models.TextField()
    calificacion = models.IntegerField()  # 0–100
    semestre = models.CharField(max_length=20, default='2025-1')
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre_materia} ({self.semestre})"
