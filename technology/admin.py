from django.contrib import admin
from .models import TheVergeDatabase
from .models import CnetDatabase
from .models import MashableDatabase
from .models import RecodeDatabase
from .models import GizmodoDatabase

# Register your models here.

admin.site.register(TheVergeDatabase)
admin.site.register(CnetDatabase)
admin.site.register(MashableDatabase)
admin.site.register(RecodeDatabase)
admin.site.register(GizmodoDatabase)
