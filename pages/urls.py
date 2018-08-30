from django.conf.urls import patterns, url 
from django.conf import settings
from pages import views

urlpatterns = patterns('',
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^about/', views.AboutView.as_view(), name='about'),
	url(r'^community/', views.CommunityView.as_view(), name='community'),
	url(r'^get_involved/', views.Get_InvolvedView.as_view(), name='involved'),
	url(r'^contact/', views.ContactView.as_view(), name='contact'),
)