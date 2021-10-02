#-*- coding: utf-8 -*-
#comment added
from __future__ import unicode_literals
from django.shortcuts import render, render_to_response
from django.http import Http404
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
# from django.contrib.auth.decorators import login_required
from django.conf import settings
from forms import MemberForm
from web.models import Setting, HomePage, Page, HomeBox, Quote, BlogPost, Member

def index(request):
	try:
		model_settings = Setting.objects.get()
	except Setting.DoesNotExist:
		model_settings = None
	try:
		model_homepage = HomePage.objects.get()
	except HomePage.DoesNotExist:
		model_homepage = None
	try:
		random_quote = Quote.objects.order_by('?').first()
	except:
		random_quote = None

	data = {
		'static_url': settings.STATIC_FILE_URL_BASE,
		'settings': model_settings,
		'homepage': model_homepage,
		'pages': Page.objects.all(),
		'homeboxes': HomeBox.objects.all(),
		'quote': random_quote,
	}

	return render(request, 'index.html', data)

def blog_post(request, slug):
	try:
		model_settings = Setting.objects.get()
	except Setting.DoesNotExist:
		model_settings = None
	try:
		blog_post = BlogPost.objects.get(slug=slug)
	except BlogPost.DoesNotExist:
		raise Http404
	data = {
		'static_url': settings.STATIC_FILE_URL_BASE,
		'settings': model_settings,
		'pages': Page.objects.all(),
		'post': blog_post,
	}

	return render(request, 'blog_post.html', data)

def blog(request):
	try:
		model_settings = Setting.objects.get()
	except Setting.DoesNotExist:
		model_settings = None

	data = {
		'static_url': settings.STATIC_FILE_URL_BASE,
		'settings': model_settings,
		'pages': Page.objects.all(),
		'posts': BlogPost.objects.order_by('-date'),
	}

	return render(request, 'blog.html', data)

def profile(request, nickname):
	try:
		model_settings = Setting.objects.get()
	except Setting.DoesNotExist:
		model_settings = None
	try:
		current_member = Member.objects.get(nickname=nickname)
	except Member.DoesNotExist:
		raise Http404

	data = {
		'static_url': settings.STATIC_FILE_URL_BASE,
		'settings': model_settings,
		'pages': Page.objects.all(),
		'member': current_member,
	}

	return render(request, 'profile.html', data)

def members(request):
	try:
		model_settings = Setting.objects.get()
	except Setting.DoesNotExist:
		model_settings = None
	data = {
		'static_url': settings.STATIC_FILE_URL_BASE,
		'settings': model_settings,
		'pages': Page.objects.all(),
		'members': Member.objects.order_by('name'),
	}

	return render(request, 'members.html', data)

# @login_required(login_url='/admin/')
def member_form(request):
	try:
		model_settings = Setting.objects.get()
	except Setting.DoesNotExist:
		model_settings = None
	data = {
		'static_url': settings.STATIC_FILE_URL_BASE,
		'settings': model_settings,
		'pages': Page.objects.all(),
		'form': MemberForm,
	}

	return render(request, 'member_form.html', data)

def member_form_submit(request):
	try:
		model_settings = Setting.objects.get()
	except Setting.DoesNotExist:
		model_settings = None

	if request.method == 'GET':
		data = {
			'static_url': settings.STATIC_FILE_URL_BASE,
			'settings': model_settings,
			'pages': Page.objects.all(),
			'form': MemberForm(),
		}

		return render(request, 'member_form.html', data)

	if request.method == 'POST':
		form = MemberForm(request.POST)
		if form.is_valid():
			data = request.POST.dict()
			body = 'MarmaraGNU için yeni bir üyelik başvurusu var!\n\n\n'
			body += 'Nickname: ' + form.cleaned_data['nickname'] + '\n\n'
			body += 'Ad soyad: ' + form.cleaned_data['name'] + '\n\n'
			body += 'E-posta: ' + form.cleaned_data['email'] + '\n\n'
			body += 'E-posta görünürlüğü: ' + form.cleaned_data['email_visibility'] + '\n\n'
			if 'institution' in request.POST:
				body += 'Okuduğu/Çalıştığı kurum: ' + form.cleaned_data['institution'] + '\n\n'
			if 'department' in request.POST:
				body += 'Okuduğu bölüm/Pozisyon: ' + form.cleaned_data['department'] + '\n\n'
			if 'irc' in request.POST:
				body += 'IRC nickname: ' + form.cleaned_data['irc'] + '\n\n'
			if 'twitter' in request.POST:
				body += 'Twitter kullanıcı adı: ' + form.cleaned_data['twitter'] + '\n\n'
			if 'github' in request.POST:
				body += 'Github kullanıcı adı: ' + form.cleaned_data['github'] + '\n\n'
			if 'teams' in request.POST:
				body += 'Yer almak istediği ekip(ler):\n'
				for team in form.cleaned_data['teams']:
					body += team + ', '
				body += '\n\n'
			if 'description' in request.POST:
				body += 'Detaylar: ' + form.cleaned_data['description']
			send_mail(
				'Üyelik Başvuru Formu',
				body,
				'MarmaraGNU <mail@mgnu.org>',
				['mail@mgnu.org'],
				fail_silently=True
			)
			return_data = {
				'static_url': settings.STATIC_FILE_URL_BASE,
				'settings': model_settings,
				'pages': Page.objects.all(),
				'form': MemberForm(),
				'success_message': 'Başvurunuz işleme alındı. Kısa bir süre sonra sizinle iletişime geçeceğiz. Teşekkürler.',
			}

			return render(request, 'member_form.html', return_data)
		else:
			data = {
				'static_url': settings.STATIC_FILE_URL_BASE,
				'settings': model_settings,
				'pages': Page.objects.all(),
				'form': MemberForm(request.POST),
				'error_message': 'Lütfen gerekli alanları doldurunuz.',
			}

			return render(request, 'member_form.html', data)

def page(request, slug):
	try:
		model_settings = Setting.objects.get()
	except Setting.DoesNotExist:
		model_settings = None
	try:
		current_page = Page.objects.get(slug=slug)
	except Page.DoesNotExist:
		raise Http404

	data = {
		'static_url': settings.STATIC_FILE_URL_BASE,
		'settings': model_settings,
		'pages': Page.objects.all(),
		'page': current_page,
	}

	return render(request, 'page.html', data)
#commented
