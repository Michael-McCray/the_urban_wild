from django.db import models

# Create your models here.
from django.db import models
from adminsortable.models import SortableMixin
# Create your models here.

class Event(SortableMixin):
	title = models.CharField(max_length=255)
	image = models.ImageField(upload_to='team/profiles')
	prev_text = models.TextField(blank=True)
	link = models.URLField(blank=False)
	is_local = models.BooleanField(default=False)
	active = models.BooleanField(default=False)
	order = models.PositiveIntegerField(default=0, editable=False, db_index=True)


	class Meta:
		ordering = ['order']


	def __unicode__(self):
		return self.title

class Article(SortableMixin):
	title = models.CharField(max_length=255)
	image = models.ImageField(upload_to='team/profiles')
	prev_text = models.TextField(blank=True)
	link = models.URLField(blank=False)
	active = models.BooleanField(default=False)
	order = models.PositiveIntegerField(default=0, editable=False, db_index=True)


	class Meta:
		ordering = ['order']


	def __unicode__(self):
		return self.title
