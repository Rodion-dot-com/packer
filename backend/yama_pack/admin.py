from django.contrib import admin

from yama_pack.models import Pack, RepackingCargotype, Status

admin.site.register(Status)
admin.site.register(Pack)
admin.site.register(RepackingCargotype)
