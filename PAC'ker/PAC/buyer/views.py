from django.shortcuts import render
from django.http import request
from seller.models import Shop
def buy(request):
 obj=Shop.objects.all()
 l=[]
 st=""
 sn=""
 for o in obj:
  st+=o.p+"\n"
  sn+=o.sname+" "+o.sid+"\t"
 l=st.split("\n")
 s=sn.split("\t")
 for i in range(len(s)):
  s[i]=s[i].split(" ")
 for i in range(len(l)):
  l[i]=l[i].split("\t")
  for j in range(len(l[i])):
   l[i][j]=l[i][j].split(" ")
 print(l)
 print(s)
 return render(request,'buyer.html',{'array':l,'array2':s})
# Create your views here.
