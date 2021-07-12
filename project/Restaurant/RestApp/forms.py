#from django.forms import ModelForm
from RestApp.models import Restaurant,Itemlist,User,Rolereq
from django import forms
# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm

class ReForm(forms.ModelForm):
	class Meta:
		model = Restaurant
		fields = ["Rname","Nitems","timings","rsimg","Address"]
		widgets = {
		"Rname":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Enter Restaurant name"}),
		"Nitems":forms.NumberInput(attrs={"class":"form-control my-2","placeholder":"Enter the number of items"}),
		"timings":forms.TimeInput(attrs={"class":"form-control my-2","placeholder":"Enter the timings","type":"time",}),
		"Address":forms.Textarea(attrs={"class":"form-control my-2","placeholder":"Enter Address","rows":5}),
		}

class ItemForm(forms.ModelForm):
	class Meta:
		model = Itemlist
		fields = ["rsid","iname","icategory","price","itavailability","iimage"]
		widgets = {
		"rsid":forms.Select(attrs={"class":"form-control my-2","placeholder":"Restaurant","readonly":True}),
		"iname":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Enter Item name"}),
		"icategory":forms.Select(attrs={"class":"form-control my-2","placeholder":"Enter Item names"}),
		"price":forms.NumberInput(attrs={"class":"form-control my-2","placeholder":"Enter price"}),
		"itavailability":forms.Select(attrs={"class":"form-control my-2",}),
		}

class UsgForm(UserCreationForm):
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Enter password"}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Enter confirm password"}))
	class Meta:
		model=User
		fields=["username"]
		widgets={
		"username":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Enter Username"}),
		}

class Rltype(forms.ModelForm):
	class Meta:
		model = Rolereq
		fields = ["uname","rltype","pfe"]
		widgets = {
		"rltype":forms.Select(attrs={
			"class":"form-control my-2",
			}),
		}

class Rlupd(forms.ModelForm):
	class Meta:
		model=User
		fields=["username","role"]
		widgets={
		"username":forms.TextInput(attrs={"class":"form-control my-2","readonly":True}),
		"role":forms.Select(attrs={"class":"form-control my-2"}),
		}

class Pfupd(forms.ModelForm):
	class Meta:
		model = User
		fields = ["username","first_name","last_name","email","age","mobilenumber","Uimg"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control my-2",
			"readonly":True,
			}),
		"first_name":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Update First Name",
			}),
		"last_name":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Update Last Name",
			}),
		"email":forms.EmailInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Update Email",
			}),
		"age":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Update Age",
			}),
		"mobilenumber":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Update Mobile Number",
			}),
		}

class Chgepwd(PasswordChangeForm):
	old_password = forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control my-2","placeholder":"Enter Old Password"
		}))
	new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control my-2","placeholder":"Enter New Password",
		}))
	new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control my-2","placeholder":"Enter New Confirm Password",
		}))
	class Meta:
		model = User
		fields = ["old_password","new_password1","new_password2"]