from django.db import models


class Unit(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = "units"
        
    def __str__(self) -> str:
        return self.name


class Text(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='words')
    content = models.TextField(max_length=50)
    audio = models.FileField(upload_to="audios")
    class Meta:
        db_table = "texts"
    