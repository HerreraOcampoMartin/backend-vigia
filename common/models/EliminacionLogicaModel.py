from django.db import models

class EliminacionLogicaModel(models.Model):
    eliminado = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False):
        self.eliminado = True
        self.save()