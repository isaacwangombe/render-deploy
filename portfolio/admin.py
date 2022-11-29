from django.contrib import admin
from .models import Projects, Databases, Comments, Languages, Frameworks, Tools
# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
  filter_horizontal=('database','languages','frameworks','tools')

admin.site.register (Projects, ProjectAdmin)
admin.site.register (Databases)
admin.site.register (Comments)
admin.site.register (Languages)
admin.site.register (Frameworks)
admin.site.register (Tools)