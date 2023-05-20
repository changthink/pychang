from django.contrib import admin
from .models import Abase, Adetail

admin.site.register([Abase, Adetail])