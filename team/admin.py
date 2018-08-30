from django.contrib import admin
from team.models import Team
from adminsortable.admin import SortableAdmin
# Register your models here.


class TeamAdmin(SortableAdmin):
	model = Team

admin.site.register(Team, TeamAdmin)

