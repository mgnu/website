from __future__ import unicode_literals
from django.contrib import admin
from web import models
from django_summernote.admin import SummernoteModelAdmin

class HomePageAdmin(SummernoteModelAdmin):
	pass

class HomeBoxAdmin(SummernoteModelAdmin):
	pass

class BlogPostAdmin(SummernoteModelAdmin):
	pass

class QuoteAdmin(SummernoteModelAdmin):
	pass

class SettingAdmin(SummernoteModelAdmin):
	pass

class PageAdmin(SummernoteModelAdmin):
	pass

class MemberAdmin(SummernoteModelAdmin):
	pass

admin.site.register(models.HomePage, HomePageAdmin)
admin.site.register(models.HomeBox, HomeBoxAdmin)
admin.site.register(models.BlogPost, BlogPostAdmin)
admin.site.register(models.Quote, QuoteAdmin)
admin.site.register(models.Setting, SettingAdmin)
admin.site.register(models.Page, PageAdmin)
admin.site.register(models.Member, MemberAdmin)