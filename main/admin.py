from django.contrib import admin
from .models import Tut,Cat,Series
from tinymce.widgets import TinyMCE
from django.db import models
# Register your models here.
class Tuter(admin.ModelAdmin):
    fieldsets=[
        ("Title/date",{"fields":["tut_title","tut_publish"]}),
        ("URL",{"fields":["tut_link"]}),
        ("Series",{"fields":["tut_ser"]}),
        ("Content",{"fields":["tut_content"]})

    ]
    formfield_overrides={
        models.TextField:{'widget':TinyMCE()}
    }

admin.site.register(Series)
admin.site.register(Cat)
admin.site.register(Tut,Tuter)
