from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
	age = models.IntegerField(default=20)
	mobilenumber = models.CharField(max_length=10,null=True)
	Uimg = models.ImageField(upload_to='Profilepics/',default='ics.jpeg')
	t = [(1,'Guest'),(2,'Manager'),(3,'User')]
	role = models.IntegerField(choices=t,default=1)

class Rolereq(models.Model):
	f = [(2,'Manager'),(3,'User')]
	rltype = models.IntegerField(choices=f)
	pfe = models.ImageField(upload_to='Rolereqpics/',default='ics.jpeg')
	is_checked = models.BooleanField(default=False)
	uname = models.CharField(max_length=50)
	ud = models.OneToOneField(User,on_delete=models.CASCADE)


class Restaurant(models.Model):
	Rname = models.CharField(max_length=30)
	Nitems = models.IntegerField()
	timings = models.CharField(max_length=50)
	Address = models.CharField(max_length=50)
	rsimg = models.ImageField(upload_to='Restaurantimages/',default='ics.jpeg')
	uid = models.ForeignKey(User,on_delete=models.CASCADE)

	def __str__(self):
	 	return self.Rname

class Itemlist(models.Model):
	y=[('NV','Non veg'),('VG','veg'),('DF','Select Item Type')]
	p=[('AV','Available'),('NA','Not Available'),('SL','Select Availability')]
	iname = models.CharField(max_length=50)
	icategory = models.CharField(choices=y,default="DF",max_length=12)
	price = models.DecimalField(decimal_places=2,max_digits=8)
	iimage = models.ImageField(upload_to='Iteminames/',default='ics.jpeg')
	itavailability = models.CharField(choices=p,default="SL",max_length=20)
	rsid=models.ForeignKey(Restaurant,on_delete=models.CASCADE)
	

