from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Projects, Comments, Languages, Frameworks, Tools, Databases
from .serializer import ProjectSerializer, CommentsSerializer, LanguagesSerializer, FrameworksSerializer, DatabasesSerializer, ToolsSerializer
from django.http import Http404
from rest_framework import status


class ProjectList(APIView):
	def get(self, request, format=None):
		all_projects = Projects.get_all()
		serializers = ProjectSerializer(all_projects, many=True)
		return Response(serializers.data)

class LanguagesList(APIView):
	def get(self, request, format=None):
		all_items = Languages.get_all()
		serializers = LanguagesSerializer(all_items, many=True)
		return Response(serializers.data)


class FrameworksList(APIView):
	def get(self, request, format=None):
		all_items = Frameworks.get_all()
		serializers = FrameworksSerializer(all_items, many=True)
		return Response(serializers.data)

class ToolsList(APIView):
	def get(self, request, format=None):
		all_items = Tools.get_all()
		serializers = ToolsSerializer(all_items, many=True)
		return Response(serializers.data)

class DatabasesList(APIView):
	def get(self, request, format=None):
		all_items = Databases.get_all()
		serializers = DatabasesSerializer(all_items, many=True)
		return Response(serializers.data)

class ProjectByDatabase(APIView):
	def get(self, request,database, format=None):
		all_projects = Projects.filter_database(database)
		serializers = ProjectSerializer(all_projects, many=True)
		if not serializers:
					raise Http404("No MyModel matches the given query.")
		return Response(serializers.data)

class ProjectByTools(APIView):
	def get(self, request, tools, format=None):
		all_projects = Projects.filter_tools(tools)
		serializers = ProjectSerializer(all_projects, many=True)
		return Response(serializers.data)

class ProjectByLanguages(APIView):
	def get(self, request,languages, format=None):
		all_projects = Projects.filter_languages(languages)
		serializers = ProjectSerializer(all_projects, many=True)
		return Response(serializers.data)

class ProjectByFrameworks(APIView):
	def get(self, request, framework,format=None):
		all_projects = Projects.filter_framework(framework)
		serializers = ProjectSerializer(all_projects, many=True)
		return Response(serializers.data)

class ProjectById(APIView):
	def get(self, request, id,format=None):
		all_projects = Projects.get_id(id)
		serializers = ProjectSerializer(all_projects, many=False)
		return Response(serializers.data)


class CommentsList(APIView):
	def get(self, request,format=None):
		all_comments = Comments.get_all()
		serializers = CommentsSerializer(all_comments, many=True)
		return Response(serializers.data)

	def post(self, request, format=None):
			serializers = CommentsSerializer(data=request.data)
			if serializers.is_valid():
					serializers.save()
					return Response(serializers.data, status=status.HTTP_201_CREATED)
			return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)