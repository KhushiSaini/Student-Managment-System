from django.db import models

# Create your models here.

class Student(models.Model):
	studentid=models.IntegerField(primary_key=True)
	studentname=models.CharField(max_length=30)
	email=models.EmailField(max_length=200)
	address=models.TextField()
	phone=models.IntegerField()
	branch=models.CharField(max_length=40)
	attendance=models.IntegerField()
	eligibility=models.CharField(max_length=4)
	marks=models.IntegerField()
	result=models.CharField(max_length=30)
	def __str__(self):
		return str(self.studentid)+"|"+self.studentname+"|"+self.email+"|"+self.address+"|"+str(self.phone)+"|"+self.branch+"|"+str(self.attendance)+"|"+self.eligibility+"|"+str(self.marks)+"|"+self.result