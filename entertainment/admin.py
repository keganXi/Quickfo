from django.contrib import admin
from .models import BBCDatabase
from .models import IOLDatabase
from .models import TheGuardianDatabase
from .models import TimeDatabase
from .models import XXLMagDatabase

# Register your models here.
admin.site.register(BBCDatabase)
admin.site.register(IOLDatabase)
admin.site.register(TheGuardianDatabase)
admin.site.register(TimeDatabase)
admin.site.register(XXLMagDatabase)

