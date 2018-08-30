from django.db import models
from team.models import Team

class Slide(models.Model):
	title = models.CharField(max_length=255, blank=False)
	tagline = models.CharField(max_length=255, blank=False)
	image = models.ImageField(upload_to="stats/image", blank=True)
	image_alt = models.CharField(max_length=255, blank=True)
	button_active = models.BooleanField(default=False, help_text='activate to show on site')
	button1_text = models.CharField(max_length=255, blank=True)
	button1_link = models.URLField(blank=True)
	button2_text = models.CharField(max_length=255, blank=True)
	button2_link = models.URLField(blank=True)
	active = models.BooleanField(default=False, help_text='activate to show on site')
	published = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.title

class Homepage(models.Model):
	title = models.CharField(max_length=255, blank=False)
	banner_slides = models.ManyToManyField(Slide)
	banner_image = models.ImageField(upload_to="homepage/banner", blank=False)
	what_we_do_title = models.CharField(max_length=255, blank=False)
	what_we_do_tagline = models.CharField(max_length=255, blank=False)
	what_we_do_center = models.ImageField(upload_to="homepage/we_do", help_text='what we do section background')
	members_title = models.CharField(max_length=255, blank=False)
	members_tagline = models.CharField(max_length=255, blank=False)
	members = models.ManyToManyField(Team)
	published = models.DateTimeField(auto_now_add=True)
	active = models.BooleanField(default=False, help_text='activate to show on site')

	def __unicode__(self):
		return self.title



class What_We_Do(models.Model):
	title = models.CharField(max_length=255, blank=False)
	text = models.CharField(max_length=255, blank=False)
	link = models.URLField(blank=False)
	right_side = models.BooleanField(default=False, help_text='activate to show on right side')
	active = models.BooleanField(default=False, help_text='activate to show on site')
	published = models.DateTimeField(auto_now_add=True)


	def __unicode__(self):
		return self.title

class Accordion_Item(models.Model):
	title = models.CharField(max_length=255, blank=False)
	text = models.TextField()
	active = models.BooleanField(default=False, help_text='activate to show on site')
	published = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.banner_title

class About(models.Model):
	banner_title = models.CharField(max_length=255, blank=False)
	banner_image = models.ImageField(upload_to="homepage/banner", blank=False)
	who_we_are_title = models.CharField(max_length=255, blank=False)
	who_we_are_tagline = models.CharField(max_length=255, blank=False)
	who_we_are_text = models.TextField()
	accordion_Items = models.ManyToManyField(Accordion_Item)
	members = models.ManyToManyField(Team)
	team_title = models.CharField(max_length=255, blank=False)
	team_tagline = models.CharField(max_length=255, blank=False)
	active = models.BooleanField(default=False, help_text='activate to show on site')
	published = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.banner_title

class Community(models.Model):
	banner_title = models.CharField(max_length=255, blank=False)
	banner_tagline = models.CharField(max_length=255, blank=False)
	banner_image = models.ImageField(upload_to="homepage/banner", blank=False)
	our_events_title = models.CharField(max_length=255, blank=False)
	local_events_title = models.CharField(max_length=255, blank=False)
	blog_title = models.CharField(max_length=255, blank=False)
	host_title = models.CharField(max_length=255, blank=False)
	host_text = models.TextField()
	host_button_text = models.CharField(max_length=255, blank=False)
	host_button_link = models.URLField(blank=False)
	active = models.BooleanField(default=False, help_text='activate to show on site')
	published = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.banner_title


