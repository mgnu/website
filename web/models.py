from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.contrib import auth

@python_2_unicode_compatible
class Setting(models.Model):
	name = models.CharField(max_length=255, default='MarmaraGNU')
	logo = models.ImageField(null=True)
	html_lang = models.CharField(max_length=2, default='tr')
	charset = models.CharField(max_length=20, default='utf-8')
	meta_viewport = models.CharField(max_length=255, default='width=device-width, initial-scale=1.0', null=True, blank=True)
	meta_description = models.CharField(max_length=255, null=True, blank=True)
	meta_author = models.CharField(max_length=255, default='MarmaraGNU', blank=True)
	meta_keywords = models.CharField(max_length=255, null=True, blank=True)
	footer = models.TextField()
	social_github = models.CharField(max_length=255, default=None, null=True, blank=True)
	social_twitter = models.CharField(max_length=255, default=None, null=True, blank=True)

	def __str__(self):
		return self.name

@python_2_unicode_compatible
class HomePage(models.Model):
	featured_image = models.ImageField(null=True, blank=True)
	featured_title = models.CharField(max_length=255)
	featured_content = models.TextField()
	featured_button = models.CharField(max_length=255, blank=True)

	def __str__(self):
		return self.featured_title

@python_2_unicode_compatible
class HomeBox(models.Model):
	title = models.CharField(max_length=255)
	content = models.TextField()
	button = models.CharField(max_length=255, default='Devamini oku', blank=True)

	def __str__(self):
		return self.title

@python_2_unicode_compatible
class Quote(models.Model):
	quote = models.TextField()

	def __str__(self):
		return self.quote

@python_2_unicode_compatible
class BlogPost(models.Model):
	featured_image = models.ImageField(null=True, blank=True)
	title = models.CharField(max_length=255)
	slug = models.SlugField(max_length=255, default='')
	content = models.TextField()
	date = models.DateTimeField(auto_now=True)
	author = models.ForeignKey('auth.User')
	tags = models.CharField(max_length=255, null=True, blank=True)

	def __str__(self):
		return self.title

@python_2_unicode_compatible
class Page(models.Model):
	slug = models.SlugField(max_length=255)
	title = models.CharField(max_length=255)
	content = models.TextField()
	keywords = models.CharField(max_length=255, blank=True)

	def __str__(self):
		return self.title

@python_2_unicode_compatible
class Member(models.Model):
	picture = models.ImageField(null=True, blank=True)
	nickname = models.CharField(max_length=100)
	name = models.CharField(max_length=100)
	role = models.CharField(max_length=100, blank=True)
	content = models.TextField(blank=True)
	email = models.EmailField(blank=True)
	irc = models.CharField(max_length=255, blank=True)
	twitter_username = models.CharField(max_length=255, blank=True)
	github_username = models.CharField(max_length=255, blank=True)

	def __str__(self):
		return self.name
