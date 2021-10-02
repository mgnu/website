#-*- coding: UTF-8 -*-
#updated program
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field
from crispy_forms.bootstrap import FormActions

error_messages = {
    'required': 'Bu alan gereklidir.',
}

class MemberForm(forms.Form):
	nickname = forms.CharField(
		label = 'Nickname',
		max_length = 100,
		required = True,
		error_messages=error_messages,
	)

	name = forms.CharField(
		label = 'Ad soyad',
		max_length = 100,
		required = True,
		error_messages=error_messages,
	)

	email = forms.EmailField(
		label = 'E-posta',
		required = True,
		error_messages=error_messages,
	)

	email_visibility = forms.ChoiceField(
		label = '',
		choices = (
			('visible', 'E-posta adresimin yayınlanmasında sakınca yoktur.'),
			('invisible', 'E-posta adresimin yayınlanmasın.'),
		),
		widget = forms.RadioSelect,
		initial = 'visible',
	)

	institution = forms.CharField(
		label = 'Okuduğunuz/Çalıştığınız kurum',
		required = False,
	)

	department = forms.CharField(
		label = 'Okuduğunuz bölüm/Pozisyonunuz',
		required = False,
	)

	irc = forms.CharField(
		label = 'IRC nickname',
		required = False,
	)

	twitter = forms.CharField(
		label = 'Twitter kullanıcı adınız',
		required = False,
	)

	github = forms.CharField(
		label = 'Github kullanıcı adınız',
		required = False,
	)

	teams = forms.MultipleChoiceField(
		label = 'Yer almak istediğiniz ekip(ler)',
		choices = (
			('project', 'Proje ekibi'),
			('translation', 'Çeviri ekibi'),
			('event', 'Etkinlik ekibi'),
		),
		widget = forms.CheckboxSelectMultiple,
		required = False,
	)

	description = forms.CharField(
		label = 'Eklemek istedikleriniz',
		widget = forms.Textarea(),
		required = False,
	)

	helper = FormHelper()
	helper.form_tag = False
	helper.form_class = 'form-horizontal'
	helper.label_class = 'col-md-2'
	helper.field_class = 'col-md-8'
	helper.layout = Layout(
		Field('nickname', css_class='form-control', style='margin-bottom: 25px'),
		Field('name', css_class='form-control', style='margin-bottom: 25px'),
		Field('email', css_class='form-control', style='margin-bottom: 5px'),
		Field('email_visibility', style='padding-left: 25px; margin-bottom: 25px'),
		Field('institution', css_class='form-control', style='margin-bottom: 25px'),
		Field('department', css_class='form-control', style='margin-bottom: 25px'),
		Field('irc', css_class='form-control', style='margin-bottom: 25px'),
		Field('twitter', css_class='form-control', style='margin-bottom: 25px'),
		Field('github', css_class='form-control', style='margin-bottom: 25px'),
		Field('teams', style='padding-left: 30px; margin-bottom: 25px'),
		Field('description', rows='3', css_class='form-control', style='margin-bottom: 25px'),
		FormActions(
			Submit('send', 'Formu Gonder', css_class='btn-primary', style='margin-bottom: 25px'),
		)
	)
