#-*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, render_to_response
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
# from django.contrib.auth.decorators import login_required
from django.conf import settings
from forms import MemberForm
from web import models

def index(request):
	data = {
		'static_url': settings.STATIC_FILE_URL_BASE,
		'settings': models.Setting.objects.get(),
		'homepage': models.HomePage.objects.get(),
		'pages': models.Page.objects.all(),
		'homeboxes': models.HomeBox.objects.all(),
		'quote': models.Quote.objects.order_by('?').first(),
	}

	return render(request, 'index.html', data)

def blog_post(request, slug):
	data = {
		'static_url': settings.STATIC_FILE_URL_BASE,
		'settings': models.Setting.objects.get(),
		'pages': models.Page.objects.all(),
		'post': models.BlogPost.objects.get(slug=slug),
	}

	return render(request, 'blog_post.html', data)

def blog(request):
	data = {
		'static_url': settings.STATIC_FILE_URL_BASE,
		'settings': models.Setting.objects.get(),
		'pages': models.Page.objects.all(),
		'posts': models.BlogPost.objects.order_by('-date'),
	}

	return render(request, 'blog.html', data)

def profile(request, nickname):
	data = {
		'static_url': settings.STATIC_FILE_URL_BASE,
		'settings': models.Setting.objects.get(),
		'pages': models.Page.objects.all(),
		'member': models.Member.objects.get(nickname=nickname),
	}

	return render(request, 'profile.html', data)

def members(request):
	data = {
		'static_url': settings.STATIC_FILE_URL_BASE,
		'settings': models.Setting.objects.get(),
		'pages': models.Page.objects.all(),
		'members': models.Member.objects.order_by('name'),
	}

	return render(request, 'members.html', data)

# @login_required(login_url='/admin/')
def member_form(request):
	data = {
		'static_url': settings.STATIC_FILE_URL_BASE,
		'settings': models.Setting.objects.get(),
		'pages': models.Page.objects.all(),
		'form': MemberForm,
	}

	return render(request, 'member_form.html', data)

def member_form_submit(request):
	if request.method == 'GET':
		data = {
			'static_url': settings.STATIC_FILE_URL_BASE,
			'settings': models.Setting.objects.get(),
			'pages': models.Page.objects.all(),
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
				'settings': models.Setting.objects.get(),
				'pages': models.Page.objects.all(),
				'form': MemberForm(),
				'success_message': 'Başvurunuz işleme alındı. Kısa bir süre sonra sizinle iletişime geçeceğiz. Teşekkürler.',
			}

			return render(request, 'member_form.html', return_data)
		else:
			data = {
				'static_url': settings.STATIC_FILE_URL_BASE,
				'settings': models.Setting.objects.get(),
				'pages': models.Page.objects.all(),
				'form': MemberForm(request.POST),
				'error_message': 'Lütfen gerekli alanları doldurunuz.',
			}

			return render(request, 'member_form.html', data)

def page(request, slug):
	data = {
		'static_url': settings.STATIC_FILE_URL_BASE,
		'settings': models.Setting.objects.get(),
		'pages': models.Page.objects.all(),
		'page': models.Page.objects.get(slug=slug),
	}

	return render(request, 'page.html', data)
