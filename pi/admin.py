from django.contrib import admin

from .models import InputFeature

from .models import OutputFeature


# Register your models here.
admin.site.register(InputFeature)
admin.site.register(OutputFeature)
