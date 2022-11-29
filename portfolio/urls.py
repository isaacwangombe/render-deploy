from django.urls import path, include
from . import views, api_views



urlpatterns = [
  path('', views.welcome,name = 'test'),


  path('api/all_projects/', api_views.ProjectList.as_view()),
  path('api/all_frameworks/', api_views.FrameworksList.as_view()),
  path('api/all_tools/', api_views.ToolsList.as_view()),
  path('api/all_languages/', api_views.LanguagesList.as_view()),
  path('api/all_databases/', api_views.DatabasesList.as_view()),
  path('api/all_comments/', api_views.CommentsList.as_view()),
  path('api/database_projects/<database>', api_views.ProjectByDatabase.as_view()),
  path('api/tools_projects/<tools>', api_views.ProjectByTools.as_view()),
  path('api/languages_projects/<languages>', api_views.ProjectByLanguages.as_view()),
  path('api/framework_projects/<framework>', api_views.ProjectByFrameworks.as_view()),
  path('api/id_projects/<id>', api_views.ProjectById.as_view()),

]
