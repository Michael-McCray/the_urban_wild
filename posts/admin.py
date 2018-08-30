from django.contrib import admin
from posts.models import Event, Article
from adminsortable.admin import SortableAdmin
# Register your models here.


class ArticleAdmin(SortableAdmin):
	model = Article

class EventAdmin(SortableAdmin):
	model = Event

admin.site.register(Event, EventAdmin)
admin.site.register(Article, ArticleAdmin)
