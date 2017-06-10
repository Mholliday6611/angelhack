from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.conf import settings
from forms import SubscribersForm, CarForm
import requests

# Create your views here.


# def index(request):
# 	if request.method == "POST":
# 		form = SubscribersForm(request.POST)

# 		if form.is_valid():
# 			sub = form.save(commit=True)
# 			sub.email = request.POST['email']
# 			sub.name = request.POST.get('first_name')
# 			send_mail(
# 				subject='Hello from SparkPost',
# 				message='Woo hoo! Sent from !',
# 				from_email='testing@sparkpostbox.com',
# 				recipient_list=[sub.email],
# 				html_message='<p>Hello Rock stars!</p>',
# 				)
# 			return HttpResponseRedirect("https://www.facebook.com/")
# 		else:
# 			print form.errors


# 	else:
# 		form = SubscribersForm()

# 	return render(request, "home/index.html", {'form': form})

# 	

def index(request):
	form_class = CarForm
	form = form_class(request.POST or None)
	if request.method == "POST":
		
		if form.is_valid():
			car = form.cleaned_data['car']

			url = "https://api.restb.ai/classify"
			querystring = {"client_key":"630baac25e972c9f607047fdc7498322b7adca6469de70684eb9b99a6dae9f4c",
			"model_id":"car_make_model",
			"image_url":car}
			response = requests.request("GET", url, params=querystring)
			print response.text
	else:
		form = CarForm()


	return render(request, "home/index.html", {"form":form, 'form_class':form_class})