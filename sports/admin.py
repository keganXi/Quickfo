from django.contrib import admin
from .models import FoxSportsDatabase
from .models import TheGuardianDatabase
from .models import BBCSportsDatabase
from .models import TheIndependentDatabase

# Register your models here.
admin.site.register(FoxSportsDatabase)
admin.site.register(TheGuardianDatabase)
admin.site.register(BBCSportsDatabase)
admin.site.register(TheIndependentDatabase)
