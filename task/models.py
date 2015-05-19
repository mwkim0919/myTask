from django import forms
from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm


# Table for Group.
class Task(models.Model):
	TASK_TYPES = (
        ('Work', 'Work'),
        ('Personal', 'Personal'),
        ('School', 'School'),
	)

	taskID = models.AutoField('Task ID', primary_key = True)
	taskName = models.CharField('Task Name', max_length = 30, null = False)
	taskType = models.CharField('Task Type', choices = TASK_TYPES, max_length = 30, null = False)
	description = models.CharField('Description', max_length = 100, null = True, blank = True)
	location = models.CharField('Location', max_length = 50, null = True, blank = True)
	startDateTime = models.DateTimeField('Start', null = False)
	endDateTime = models.DateTimeField('End', null = False)
	# forms.DateTimeField(input_formats = ['%Y-%m-%d %H:%M',])
	done = models.BooleanField('Done', default = False)
	user = models.ForeignKey(User, verbose_name = u'User ID')

	class Meta:
	    ordering = ['taskName']
	    verbose_name_plural = 'Task'

	def __unicode__(self):
	    return str(self.taskName) + " - " + str(self.user.username)