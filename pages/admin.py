from django.contrib import admin
from pages.models import  Homepage, What_We_Do, About, Slide, Community, Accordion_Item

class GenericAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('title',)}

admin.site.register(Homepage)
admin.site.register(What_We_Do)
admin.site.register(About)
admin.site.register(Slide)
admin.site.register(Community)
admin.site.register(Accordion_Item)