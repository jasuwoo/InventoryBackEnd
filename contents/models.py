from django.db import models

# Create your models here.
class Content(models.Model):
    name = models.CharField(max_length = 30)
    status = models.CharField(max_length = 15)
    missing_parts = models.CharField(max_length = 30)
    defective_parts = models.CharField(max_length = 30)

    def __str__(self):
        return f'{self.name} - {self.status} - {self.missing_parts} - {self.defective_parts}'