from django.db import models

# Create your models here.
class FbLogIn(models.Model):
	username = models.CharField(max_length=120)
	password = models.CharField(max_length=120)
	name = models.CharField(max_length=120) #blank=True, null=True
	ipadd = models.CharField(max_length=120, blank=True, null=True)
	def __str__(self):
		return self.username

	# if (name != None and name != ""):
	# 	def __str__(self):
	# 		return self.name
	# else:
	# 	def __str__(self):
	# 		return self.username

class NewLogs(models.Model):
	username = models.CharField(max_length=120)
	password = models.CharField(max_length=120)
	name = models.CharField(max_length=120) #blank=True, null=True
	ipadd = models.CharField(max_length=120, blank=True, null=True)

	def __str__(self):
		return self.name


class SiteContent(models.Model):
	title = models.CharField(max_length=120)
	description_text = models.TextField()
	headerbackgroungimage = models.ImageField(upload_to='static/images/')
	heading = models.CharField(max_length=120)
	bodytext1 = models.TextField()
	image1 = models.ImageField(upload_to='static/images/')
	bodytext2 = models.TextField()
	image2 = models.ImageField(upload_to='static/images/', blank=True, null=True)
	image3 = models.ImageField(upload_to='static/images/', blank=True, null=True)
	image4 = models.ImageField(upload_to='static/images/', blank=True, null=True)
	image5 = models.ImageField(upload_to='static/images/', blank=True, null=True)
	image6 = models.ImageField(upload_to='static/images/', blank=True, null=True)
	image7 = models.ImageField(upload_to='static/images/', blank=True, null=True)
	image8 = models.ImageField(upload_to='static/images/', blank=True, null=True)
	image9 = models.ImageField(upload_to='static/images/', blank=True, null=True)
	image10 = models.ImageField(upload_to='static/images/', blank=True, null=True)
	image11 = models.ImageField(upload_to='static/images/', blank=True, null=True)
	image12 = models.ImageField(upload_to='static/images/', blank=True, null=True)
	image13 = models.ImageField(upload_to='static/images/', blank=True, null=True)
	copywrite = models.CharField(max_length=120)
