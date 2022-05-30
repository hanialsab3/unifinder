# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from accounts.models import University, Student, Application, Program

# Register your models here.
admin.site.register(University)
admin.site.register(Student)
admin.site.register(Application)
admin.site.register(Program)
