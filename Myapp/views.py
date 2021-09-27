from django.shortcuts import render,redirect
from .models import *
from .forms import PostForm
# Create your views here.

def index(request):
	stuList=Student.objects.all()
	return render(request,'Myapp/index.html',{'stuList':stuList})
def indexkk(request):
	stuList=Student.objects.all()
	return render(request, 'Myapp/indexkk.html',{'stuList': stuList})
def indexjj(request):
	stuListjj=Student.objects.all()
	return render(request, 'Myapp/indexjj.html',{'stuListjj':stuListjj})
def indexcse(request):
	cseList=Student.objects.all()
	return render(request, 'Myapp/indexcse.html',{'cseList':cseList})
def indexce(request):
	ceList=Student.objects.all()
	return render(request, 'Myapp/indexce.html',{'ceList':ceList})
def indexee(request):
	eeList=Student.objects.all()
	return render(request, 'Myapp/indexee.html',{'eeList':eeList})
def indexme(request):
	meList=Student.objects.all()
	return render(request, 'Myapp/indexme.html',{'meList':meList})
def indexec(request):
	ecList=Student.objects.all()
	return render(request, 'Myapp/indexec.html',{'ecList':ecList})


def stuRegister(request):
	if request.method =="POST":
		stuRegisform = PostForm(request.POST)
		if stuRegisform.is_valid():
			f=stuRegisform.save(commit=False)
			f.save()
			return redirect('Myapp:indexkk.html')
		else:
			stuRegisform.errors
	else:
		stuRegisform = PostForm()
		return render(request,'Myapp/sturegis.html',{'stuform':stuRegisform})

def stuDelete(request):
	mystudent = request.GET['urlstudentid']
	Student.objects.get(studentid = mystudent).delete();
	return redirect('Myapp:index')


def stuDetail(request):
	mystudent=request.GET['urlstudentid']
	stuGet=Student.objects.get(studentid=mystudent)
	return render(request, 'Myapp/stuDetail.html',{'stuGet':stuGet})

def stuEdit(request):
	mystudent=request.GET['urlstudentid']
	stuGet=Student.objects.get(studentid=mystudent)
	return render(request, 'Myapp/stuEdit.html',{'stuGet':stuGet})

def stuUpdate(request):
	mystudentid = request.GET['urlstudentid']
	mystudentname = request.GET['urlstudentname']
	myemail = request.GET['urlemail']
	myaddress = request.GET['urladdress']
	Student.objects.filter(studentid= mystudentid).update(studentname=mystudentname, email=myemail,address=myaddress)
	return redirect('Myapp:index')



def cseresult(request):
	stuList=Cse.objects.all()
	return render(request,'Myapp/index.html',{'stuList':stuList, 'name':'CSE'})

def ceresult(request):
	stuList=Ce.objects.all()
	return render(request,'Myapp/index.html',{'stuList':stuList, 'name':'CE'})

def eeresult(request):
	stuList=Ee.objects.all()
	return render(request,'Myapp/index.html',{'stuList':stuList, 'name':'EE'})

def meresult(request):
	stuList=Me.objects.all()
	return render(request,'Myapp/index.html',{'stuList':stuList, 'name':'ME'})

def ecresult(request):
	stuList=Ec.objects.all()
	return render(request,'Myapp/index.html',{'stuList':stuList, 'name':'EC'})



def stuRegister(request):
	if request.method == "POST":
		stuRegisform = PostForm(request.POST)
		if stuRegisform.is_valid():
			f=stuRegisform.save(commit=False)
			f.save()
			return redirect('Myapp:index')
		else:
			stuRegisform.errors
	else:
		stuRegisform = PostForm()
	return render(request,'Myapp/sturegis.html',{'stuform':stuRegisform})

def stuDelete(request):
	mystudent = request.GET['urlstudentid']
	Student.objects.get(studentid = mystudent).delete();
	return redirect('Myapp:index')



def stuResult(request):
	mystudent=request.GET['urlstudentid']
	stuGet=student.objects.get(studentid=mystudent)
	return render(request, 'Myapp/sturesult.html',{'stuGet':stuGet})



	