from rest_framework import serializers
from .models import PortfolioDatabases, PortfolioFrameworks, PortfolioLanguages, PortfolioProjects, PortfolioComments, PortfolioTools 




class LanguagesSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = PortfolioLanguages
    fields = ('id','language')


class FrameworksSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = PortfolioFrameworks
    fields = ('id','framework')

class ToolsSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = PortfolioTools
    fields = ('id','tool')

class DatabasesSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = PortfolioDatabases
    fields = ('id','database')



class ProjectSerializer(serializers.ModelSerializer):

  languages = LanguagesSerializer(many=True)
  frameworks = FrameworksSerializer(many=True)
  tools = ToolsSerializer(many=True)
  database = DatabasesSerializer(many=True)
  class Meta:
    model = PortfolioProjects
    fields = ('id','name', 'details', 'date', 'languages', 'frameworks', 'tools', 'database', 'image','link','github')

class CommentsSerializer(serializers.ModelSerializer):
  class Meta:
    model = PortfolioComments
    fields = ('name', 'email',  'comment', 'design_rating', 'content_rating', 'user_rating', 'date', 'project')

