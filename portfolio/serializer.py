from rest_framework import serializers
from .models import Databases, Frameworks, Languages, Projects, Comments, Tools 




class LanguagesSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Languages
    fields = ('id','language')


class FrameworksSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Frameworks
    fields = ('id','framework')

class ToolsSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Tools
    fields = ('id','tool')

class DatabasesSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Databases
    fields = ('id','database')



class ProjectSerializer(serializers.ModelSerializer):

  languages = LanguagesSerializer(many=True)
  frameworks = FrameworksSerializer(many=True)
  tools = ToolsSerializer(many=True)
  database = DatabasesSerializer(many=True)
  class Meta:
    model = Projects
    fields = ('id','name', 'details', 'date', 'languages', 'frameworks', 'tools', 'database', 'image','link','github')

class CommentsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comments
    fields = ('name', 'email',  'comment', 'design_rating', 'content_rating', 'user_rating', 'date', 'project')

