from django.db import models
from adminsortable.models import SortableMixin
# Create your models here.

class Team(SortableMixin):
	name = models.CharField(max_length=255)
	position = models.CharField(max_length=255)
	image = models.ImageField(upload_to='team/profiles')
	bio_text = models.TextField(blank=True)
	active = models.BooleanField(default=False)
	order = models.PositiveIntegerField(default=0, editable=False, db_index=True)


	class Meta:
		ordering = ['order']


	def __unicode__(self):
		return self.name


