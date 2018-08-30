from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from django.contrib import messages 
from pages.models import Homepage,  What_We_Do, About, Slide, Community, Accordion_Item
from team.models import Team
from posts.models import Event, Article
from django.views.generic import View, ListView, DetailView, FormView, TemplateView
# Create your views here.

class IndexView(View):
	template_name = 'index.html'

	def get(self, request, *args, **kwargs):
		context = {}
		context['page'] = Homepage.objects.filter(active=True).order_by('-published')[:1]
		context['goals'] = What_We_Do.objects.filter(active=True).order_by('-published')[:3]
	
		return  render(request, self.template_name, context)

class AboutView(View):
	template_name =  'about.html'

	def get(self, request, *args, **kwargs):
		context = {}
		context['page'] = About.objects.filter(active=True).order_by('-published')[:1]
		context['team'] = Team.objects.filter(active=True).order_by('name')

		return  render(request, self.template_name, context)

class CommunityView(View):
	template_name =  'community.html'

	def get(self, request, *args, **kwargs):
		context = {}
		context['page'] = Community.objects.filter(active=True).order_by('-published')[:1]
		context['articles'] = Article.objects.filter(active=True).order_by('-published')[:1]
		context['local_events'] = Event.objects.filter(active=True).order_by('name')
		context['events'] = Event.objects.filter(active=True, is_local=False).order_by('name')

		return  render(request, self.template_name, context)

class Get_InvolvedView(View):
	template_name =  'involved.html'
	def get(self, request, *args, **kwargs):
		context = {}

		return  render(request, self.template_name, context)

class ContactView(View):
	template_name =  'contact.html'
	def get(self, request, *args, **kwargs):
		context = {}

		return  render(request, self.template_name, context)