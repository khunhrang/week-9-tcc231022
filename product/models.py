from django.db import models

class AllProduct(models.Model):
	product_name = models.CharField(max_length=100)
	product_price = models.CharField(max_length=100)
	product_detail = models.TextField(null=True, blank=True)
	photo = models.ImageField(upload_to="assetphoto",null=True,blank=True,default='default.png')

	def __str__(self):
		return self.product_name