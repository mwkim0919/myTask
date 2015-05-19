from django.contrib import admin

from forms import *
from models import *

class TaskAdmin(admin.ModelAdmin):
	list_display = ('taskName', 'startDateTime',
		'endDateTime', 'done')

admin.site.register(Task, TaskAdmin)
