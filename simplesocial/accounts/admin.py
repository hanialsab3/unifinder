# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from accounts.models import University, Student

# Register your models here.
admin.site.register(University)
admin.site.register(Student)
