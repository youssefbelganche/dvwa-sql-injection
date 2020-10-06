from django.db import models


from django.db import models


'''  Models '''
class animal(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=80, blank=True, unique=False)
