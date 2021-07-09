from django.contrib import admin
from home.models import TheVergeDatabase
from home.models import TheIndependentDatabase
from home.models import XXLMagDatabase
from home.models import MSNBCDatabase

# Register your models here.
admin.site.register(TheVergeDatabase)
admin.site.register(TheIndependentDatabase)
admin.site.register(XXLMagDatabase)
admin.site.register(MSNBCDatabase)
