from django.shortcuts import render, HttpResponse, redirect
from copy import deepcopy
from .models import Shop 

def home(request):
 return render(request,'home.html')

def shopreg(request):
 sname=request.GET["sname"]
 address=request.GET["address"]
 sid=str(len(sname))+sname[0]+sname[1]
 o=Shop(sname=sname,sid=sid,address=address)
 o.save()
 return redirect('home')

def takin(request):
 sid=request.GET["sid"]
 n=int(request.GET["n"])
 st=""
 obj=Shop.objects.get(sid=sid)
 for i in range(1,(n+1)):
  st=st+request.GET["pn"+str(i)]+" "+str(request.GET["p"+str(i)])+" "+str(request.GET["q"+str(i)])+"\t"
 print(st)
 obj.p=obj.p+st
 obj.save()
 return redirect('home')

def updaterec(request):
 sid=request.GET["sid"]
 c=int(request.GET["c"])
 st=""
 obj=Shop.objects.get(sid=sid)
 for i in range(1,int(c)):
  st=st+request.GET["pn"+str(i)]+" "+str(request.GET["p"+str(i)])+" "+str(request.GET["q"+str(i)])+"\t"
 print(st)
 obj.p=st
 obj.save()
 return redirect('home')

def updatein(request):
 sid=request.GET["sid"]
 st=""
 obj=Shop.objects.get(sid=sid)
 l=obj.p
 l=l.split("\t")
 for i in range(len(l)):
  l[i]=l[i].split(" ")
 return render(request,'updateind.html',{'sid':sid,'list':l})

def delin(request):
 sid=request.GET["sid"]
 obj=Shop.objects.get(sid=sid)
 obj.p="	"
 obj.save()
 return redirect('home')

def shopin(request):
 return render(request,'shopinterface.html')

def adds(request):
 return render(request,'addshop.html') 

def sell(request):
 return render(request,'seller/seller.html')

def de(request):
 return render(request,'delete.html')

def up(request):
 return render(request,'update.html')
# Create your views here.
