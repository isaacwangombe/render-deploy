from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Languages(models.Model):
	language = models.CharField(max_length =30)
	def __str__(self):
		return self.language

	class Meta:
			verbose_name_plural  =  "Languages"  


	@classmethod
	def get_all(cls):
		items = cls.objects.all()
		return items


class Frameworks(models.Model):
	framework = models.CharField(max_length =30, blank=True, null=True)
	def __str__(self):
		return self.framework

	class Meta:
			verbose_name_plural  =  "Frameworks"  



	@classmethod
	def get_all(cls):
		items = cls.objects.all()
		return items

class Tools(models.Model):
	tool = models.CharField(max_length =30, blank=True, null=True)
	def __str__(self):
		return self.tool

	class Meta:
			verbose_name_plural  =  "Tools"  


	@classmethod
	def get_all(cls):
		items = cls.objects.all()
		return items

class Databases(models.Model):
	database = models.CharField(max_length =30, blank=True, null=True)
	def __str__(self):
		return self.database

	class Meta:
			verbose_name_plural  =  "Databases"  


	@classmethod
	def get_all(cls):
		items = cls.objects.all()
		return items
class Projects(models.Model):
	name = models.CharField(max_length =30)
	details = models.TextField(max_length =1000)
	link = models.CharField(max_length =150, blank=True, null=True)
	github = models.CharField(max_length =150, blank=True, null=True)
	date = models.DateField(auto_now_add=False) 
	languages = models.ManyToManyField(Languages , db_column='languages_language')
	frameworks = models.ManyToManyField(Frameworks, blank=True)
	tools = models.ManyToManyField(Tools, blank=True)
	database = models.ManyToManyField(Databases, blank=True)
	image = CloudinaryField('image')

	def __str__(self):
		return self.name

	class Meta:
			verbose_name_plural  =  "Projects"  

	@classmethod
	def get_all(cls):
		projects = cls.objects.all().order_by('-id')
		return projects

	@classmethod
	def get_id(cls, id):
		projects = cls.objects.get(id=id)
		return projects

	@classmethod
	def filter_framework(cls, framework):
		projects = cls.objects.filter(frameworks__framework=framework).order_by('-id')
		return projects

	@classmethod
	def filter_languages(cls, languages):
		projects = cls.objects.filter(languages__language=languages).order_by('-id')
		return projects

	@classmethod
	def filter_tools(cls, tools):
		projects = cls.objects.filter(tools=tools).order_by('-id')
		return projects

	@classmethod
	def filter_database(cls, database):
		projects = cls.objects.filter(database=database).order_by('-id')
		return projects




RATING = (
(1,1),
(2,2),
(3,3),
(4,4),
(5,5),

)

class Comments(models.Model):
	name = models.CharField(max_length =30)
	email = models.EmailField(max_length =30, blank=True,null=True)
	comment = models.TextField(max_length =1000, default = "Great Project")
	design_rating = models.IntegerField(choices=RATING, default=1)
	user_rating = models.IntegerField(choices=RATING, default=1)
	content_rating = models.IntegerField(choices=RATING, default=1)
	date = models.DateField(auto_now_add=True) 
	project = models.ForeignKey(Projects, on_delete=models.CASCADE)

	def __str__(self):
		return str(f"name-{self.name}, date- {self.date}")

	class Meta:
			verbose_name_plural  =  "Comments"  


	@classmethod
	def get_all(cls):
		comments = cls.objects.all()
		return comments

	@classmethod
	def filter_project(cls, project):
		projects = cls.objects.filter(project__name=project)
		return projects
