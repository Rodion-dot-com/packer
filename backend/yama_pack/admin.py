from django.contrib import admin

from yama_pack.models import Pack, Status, RepackingCargotype

admin.site.register(Status)
admin.site.register(Pack)
admin.site.register(RepackingCargotype)
