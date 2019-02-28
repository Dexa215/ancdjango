from django.contrib import admin
from .models import Socio, Tessera, CaricaSociale, Rts, Rcs, Sezione


# Register your models here.

admin.site.register(Socio)
admin.site.register(Tessera)
admin.site.register(Rts)
admin.site.register(CaricaSociale)
admin.site.register(Rcs)
admin.site.register(Sezione)