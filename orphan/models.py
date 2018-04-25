from django.db import models
from multiselectfield import MultiSelectField
# Create your models here.


class Upload_form(models.Model):
    project_name = models.CharField(max_length=60, null=False, blank=False)
    project_discription = models.TextField()
    project_stack = models.CharField(max_length=100, null=False, blank=False)
    project_link = models.URLField()
    owner_name = models.CharField(max_length=50, null=False, blank=False)
    progress = (
        ('Completed', 'Completed'), ('Not Completed', 'Not Completed'), 
        ('Just Started', 'Just Started'), ('Half Cooked','Half Cooked'),
    )
    project_progress = MultiSelectField(choices=progress)

    def __str__(self):
        return self.project_name
