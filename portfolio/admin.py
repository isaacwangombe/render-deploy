from django.contrib import admin
from .models import PortfolioProjects, PortfolioDatabases, PortfolioComments, PortfolioLanguages, PortfolioFrameworks, PortfolioTools
# Register your models here.


class ProjectAdminAdmin(admin.ModelAdmin):
  filter_horizontal=('database','languages','frameworks','tools')

admin.site.register (PortfolioProjects, ProjectAdminAdmin)
admin.site.register (PortfolioDatabases)
admin.site.register (PortfolioComments)
admin.site.register (PortfolioLanguages)
admin.site.register (PortfolioFrameworks)
admin.site.register (PortfolioTools)