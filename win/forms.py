from django import forms
from models import Subscribers

class CarForm(forms.Form):
	car = forms.ImageField()
class SubscribersForm(forms.ModelForm):
	first_name = forms.CharField(max_length=50, help_text="Enter First Name", required=True)
	last_name = forms.CharField(max_length=50, help_text="Enter Last Name")
	email = forms.EmailField(max_length=123, help_text="Enter Email", required=True)


	class Meta:
		model = Subscribers
		fields = ('first_name', 'last_name', 'email')
	# def clean_email(self):
	# 	email = self.cleaned_data.get('email')
	# 	Subscribers = Subscribers.objects.get(email=email)

		
	# 	if Subscribers.DoesNotExist:
	# 		return email
	# 	else:
	# 		raise forms.ValidationError('This email address is already in use')
	# 	return self.cleaned_data