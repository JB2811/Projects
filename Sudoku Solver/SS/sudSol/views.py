from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import copy
import random
import math
def test(request): 
 return render(request,'stemphtml/home.html')

def test1(request):
 return render(request,"stemphtml/solvefrnd.html",{'flag':0,'row':0})

def game(request):
 return render(request,"stemphtml/level.html",{})
class Sudoku:
  def __init__(self, N, K):
    self.N = N
    self.K = K

		# Compute square root of N
    SRNd = math.sqrt(N)
    self.SRN = int(SRNd)
    self.mat = [[0 for _ in range(N)] for _ in range(N)]
	
  def fillValues(self):
		# Fill the diagonal of SRN x SRN matrices
    self.fillDiagonal()

	  # Fill remaining blocks
    self.fillRemaining(0, self.SRN)

		# Remove Randomly K digits to make game
    self.removeKDigits()
    return self.mat;
	
  def fillDiagonal(self):
	  for i in range(0, self.N, self.SRN):
		  self.fillBox(i, i)
	
  def unUsedInBox(self, rowStart, colStart, num):
	  for i in range(self.SRN):
		  for j in range(self.SRN):
			  if self.mat[rowStart + i][colStart + j] == num:
				  return False
	  return True
	 
  def fillBox(self, row, col):
	  num = 0
	  for i in range(self.SRN):
		  for j in range(self.SRN):
			  while True:
				  num = self.randomGenerator(self.N)
				  if self.unUsedInBox(row, col, num):
					  break
			  self.mat[row + i][col + j] = num
	
  def randomGenerator(self, num):
	  return math.floor(random.random() * num + 1)
	
  def checkIfSafe(self, i, j, num):
	  return (self.unUsedInRow(i, num) and self.unUsedInCol(j, num) and self.unUsedInBox(i - i % self.SRN, j - j % self.SRN, num))
	
  def unUsedInRow(self, i, num):
	  for j in range(self.N):
		  if self.mat[i][j] == num:
			  return False
	  return True
	
  def unUsedInCol(self, j, num):
	  for i in range(self.N):
		  if self.mat[i][j] == num:
			  return False
	  return True
	
	
  def fillRemaining(self, i, j):
		# Check if we have reached the end of the matrix
	  if i == self.N - 1 and j == self.N:
		  return True
	
		# Move to the next row if we have reached the end of the current row
	  if j == self.N:
		  i += 1
		  j = 0
	
		# Skip cells that are already filled
	  if self.mat[i][j] != 0:
		  return self.fillRemaining(i, j + 1)
	
		# Try filling the current cell with a valid value
	  for num in range(1, self.N + 1):
		  if self.checkIfSafe(i, j, num):
			  self.mat[i][j] = num
			  if self.fillRemaining(i, j + 1):
				  return True
			  self.mat[i][j] = 0
		
		# No valid value was found, so backtrack
	  return False

  def removeKDigits(self):
	  count = self.K

	  while (count != 0):
		  i = self.randomGenerator(self.N) - 1
		  j = self.randomGenerator(self.N) - 1
		  if (self.mat[i][j] != 0):
			  count -= 1
			  self.mat[i][j] = 0
	
	  return

def easy(request):
  game=[]
  N = 9
  K = random.randint(36,46)
  sudoku=Sudoku(N, K)
  mat=sudoku.fillValues()
  i=0; j=0 
  while(i<9):
   j=0
   while(j<9):
    if(mat[i][j]==0):
     pass
    else:
     game.append([i,j,mat[i][j]])
    j=j+1
   i=i+1
  return render(request,"stemphtml/playgame.html",{'game':game}) 

def medium(request):
  game=[]
  N = 9
  K = random.randint(45,56)
  sudoku=Sudoku(N, K)
  mat=sudoku.fillValues()
  i=0; j=0 
  while(i<9):
   j=0
   while(j<9):
    if(mat[i][j]==0):
     pass
    else:
     game.append([i,j,mat[i][j]])
    j=j+1
   i=i+1
  return render(request,"stemphtml/playgame.html",{'game':game}) 

def hard(request): 
  game=[]
  N = 9
  K = random.randint(55,64)
  sudoku=Sudoku(N, K)
  mat=sudoku.fillValues()
  i=0; j=0 
  while(i<9):
   j=0
   while(j<9):
    if(mat[i][j]==0):
     pass
    else:
     game.append([i,j,mat[i][j]])
    j=j+1
   i=i+1
  return render(request,"stemphtml/playgame.html",{'game':game}) 

def t1(request):
 row=[]
 col=[]
 sud=[]
 s=sum([1,2,3,4,5,6,7,8,9])

 for i in range(0,9):
  c=list()
  for j in range(0,9):
   v=request.POST[str(i)+str(j)]
   try:
    if(v!="" and int(v)>0 and int(v)<10):
     c.append(int(v))
    elif(v==""):
     c.append(0)
   except Exception:
    flag=3
    return JsonResponse({'row':row,'flag':flag})
  for k in range(1,10):
   if(c.count(k)>1):
    flag=4
    return JsonResponse({'row':row,'flag':flag})
  row.append(copy.deepcopy(c))
 v=0  
 
 for i in range(0,9):
  c=list()
  for j in range(0,9):
   c.append(row[j][i])
  for k in range(1,10):
   if(c.count(k)>1):
    flag=5
    return JsonResponse({'row':row,'flag':flag})
  col.append(copy.deepcopy(c))
 i=0; j=0
 
 while(i<9):
  c=list()
  c1=list()
  c2=list()
  z=i+3; x=j+3
  while(i<z):
   while(j<x):
    c.append(row[i][j])
    c1.append(row[i][j+3])
    c2.append(row[i][j+6])
    j=j+1
   j=x-3
   i=i+1
  for k in range(1,10):
   if(c.count(k)>1 or c1.count(k)>1 or c2.count(k)>1):
    flag=6
    return JsonResponse({'row':row,'flag':flag})
  i-i+3
  sud.append(copy.deepcopy(c))
  sud.append(copy.deepcopy(c1))
  sud.append(copy.deepcopy(c2))

 p=1; w=0
 while(p>0):
  p=0
  
  for i in range(0,9):
   if(row[i].count(0)==1):
     p=p+1
     t=s-sum(row[i])
     q=row[i].index(0)
     row[i][row[i].index(0)]=t
     col[row[i].index(t)][i]=t
     sud[int(i/3)*3+int(q/3)][(i%3)*3+q%3]=t
   if(col[i].count(0)==1):
     p=p+1
     t=s-sum(col[i])
     q=col[i].index(0)
     col[i][col[i].index(0)]=t
     row[col[i].index(t)][i]=t
     sud[int(i/3)+int(q/3)*3][(i%3)+(q%3)*3]=t

  for i in range(0,9):
   for j in range(1,10):
    if j not in sud[i]:
     l=[]
     p=p+1

     #i%%3==0

     if(i%3==0):
      if(i==0):
       z=i+3; x=i+6
      elif(i==3):
       z=i-3; x=i+3
      else:
       z=i-6; x=i-3    
      a=[]
      if(sud[i+1].count(j)>0):
       a.append(int(sud[i+1].index(j)/3))
      if(sud[i+2].count(j)>0):
       a.append(int(sud[i+2].index(j)/3))
      b=[]

      if(sud[z].count(j)>0):
       b.append(int(sud[z].index(j)%3))

      if(sud[x].count(j)>0):
       b.append(int(sud[x].index(j)%3))

      if(len(b)==0 and len(a)==0):
       continue

      if(len(a)==2 and len(b)==2):

       for k in range(3):
        if k not in a:
         a=k
         break

       for k in range(3):
        if(k not in b):
         b=k
         break
       sud[i][a*3+b]=j;
       b=a*3+b
       row[int(i/3)*3+int(b/3)][b%3]=j
       col[b%3][int(i/3)*3+int(b/3)]=j

      elif(len(a)==2 and len(b)!=2):

       for k in range(3):

        if k not in a:
         c=k
         break

       if(sud[i][c*3:c*3+3].count(0)==1):
        a=sud[i][c*3:c*3+3].index(0)
        sud[i][c*3+a]=j
        a=c*3+a
        row[int(i/3)*3+int(a/3)][a%3]=j
        col[a%3][int(i/3)*3+int(a/3)]=j
        continue

       elif(sud[i][c*3:c*3+3].count(0)==2 and len(b)==1):
        a=sud[i][c*3:c*3+3];

        if(a[b[0]]==0):

         for k in range(3):

          if k not in b:

           if a[k]==0:
            a=k
            break
         sud[i][c*3+a]=j
         a=c*3+a
         row[int(i/3)*3+int(a/3)][a%3]=j
         col[a%3][int(i/3)*3+int(a/3)]=j
         continue

      elif(len(b)==2 and len(a)!=2):

       for k in range(3):

        if k not in b:
         c=k
         break

       if(col[(i*3+c)%9][int(i/3)*3:int(i/3)*3+3].count(0)==1):
        a=col[(i*3+c)%9][int(i/3)*3:int(i/3)*3+3].index(0)
        q=(i*3+c)%9;
        a=int(i/3)*3+a
        col[q][a]=j
        row[a][q]=j
        sud[int(q/3)+int(a/3)*3][(q%3)+(a%3)*3]=j
        continue

       elif(col[(i*3+c)%9][int(i/3)*3:int(i/3)*3+3].count(0)==2 and len(a)==1):
        b=col[(i*3+c)%9][int(i/3)*3:int(i/3)*3+3];

        if(b[a[0]]==0):

         for k in range(3):

          if k not in a:

           if b[k]==0:
            b=k
            break
         q=(i*3+c)%9
         b=int(i/3)*3+b
         col[q][b]=j
         row[b][q]=j
         sud[int(q/3)+int(b/3)*3][(q%3)+(b%3)*3]=j
         continue

      elif(len(a)==1 and len(b)==1):
       l1=[]

       for k in range(a[0]*3,a[0]*3+3):
        l1.append(k)

       for k in range(9):

        if(k%3!=b[0] and k not in l1):
         l.append(sud[i][k])

         if(sud[i][k]==0):
          a=k

       if(l.count(0)==1):
        sud[i][a]=j
        row[int(i/3)*3+int(a/3)][a%3]=j
        col[a%3][int(i/3)*3+int(a/3)]=j
        continue

      elif(len(b)==1 and len(a)==0):

       for k in range(9):

        if(k%3!=b[0]):
         l.append(sud[i][k])

         if(sud[i][k]==0):
          a=k

       if(l.count(0)==1):
        sud[i][a]=j
        row[int(i/3)*3+int(a/3)][a%3]=j
        col[a%3][int(i/3)*3+int(a/3)]=j
        continue

      elif(len(a)==1 and len(b)==0):

       for k in range(9):

        if(int(k/3)!=a[0]):
         l.append(sud[i][k])

         if(sud[i][k]==0):
          g=k

       if(l.count(0)==1):
        sud[i][g]=j
        row[int(i/3)*3+int(g/3)][g%3]=j
        col[g%3][int(i/3)*3+int(g/3)]=j
        continue

      else:
       pass

     #i%3==1

     elif(i%3==1):

      if(i==1):
       z=i+3; x=i+6

      elif(i==4):
       z=i-3; x=i+3

      else:
       z=i-6; x=i-3    

      a=[]

      if(sud[i-1].count(j)>0):
       a.append(int(sud[i-1].index(j)/3))

      if(sud[i+1].count(j)>0):
       a.append(int(sud[i+1].index(j)/3))

      b=[]

      if(sud[z].count(j)>0):
       b.append(int(sud[z].index(j)%3))

      if(sud[x].count(j)>0):
       b.append(int(sud[x].index(j)%3))

      if(len(b)==0 and len(a)==0):
       continue

      if(len(a)==2 and len(b)==2):

       for k in range(3):

        if k not in a:
         a=k
         break

       for k in range(3):

        if(k not in b):
         b=k
         break
       sud[i][a*3+b]=j;
       b=a*3+b
       row[int(i/3)*3+int(b/3)][3+b%3]=j
       col[3+b%3][int(i/3)*3+int(b/3)]=j

      elif(len(a)==2 and len(b)!=2):

       for k in range(3):

        if k not in a:
         c=k
         break

       if(sud[i][c*3:c*3+3].count(0)==1):
        a=sud[i][c*3:c*3+3].index(0)
        sud[i][c*3+a]=j
        a=c*3+a
        row[int(i/3)*3+int(a/3)][3+a%3]=j
        col[3+a%3][int(i/3)*3+int(a/3)]=j
        continue

       elif(sud[i][c*3:c*3+3].count(0)==2 and len(b)==1):
        a=sud[i][c*3:c*3+3];


        if(a[b[0]]==0):

         for k in range(3):

          if k not in b:

           if a[k]==0:
            a=k
            break
         sud[i][c*3+a]=j
         a=c*3+a
         row[int(i/3)*3+int(a/3)][3+a%3]=j
         col[3+a%3][int(i/3)*3+int(a/3)]=j
         continue

      elif(len(b)==2 and len(a)!=2):

       for k in range(3):

        if k not in b:
         c=k
         break

       if(col[(i*3+c)%9][int(i/3)*3:int(i/3)*3+3].count(0)==1):
        a=col[(i*3+c)%9][int(i/3)*3:int(i/3)*3+3].index(0)
        q=(i*3+c)%9;
        a=int(i/3)*3+a
        col[q][a]=j
        row[a][q]=j
        sud[int(q/3)+int(a/3)*3][(q%3)+(a%3)*3]=j
        continue

       elif(col[(i*3+c)%9][int(i/3)*3:int(i/3)*3+3].count(0)==2 and len(a)==1):
        b=col[(i*3+c)%9][int(i/3)*3:int(i/3)*3+3];

        if(b[a[0]]==0):

         for k in range(3):

          if k not in a:

           if b[k]==0:
            b=k
            break
         q=(i*3+c)%9
         b=int(i/3)*3+b
         col[q][b]=j
         row[b][q]=j
         sud[int(q/3)+int(b/3)*3][(q%3)+(b%3)*3]=j
         continue

      elif(len(a)==1 and len(b)==1):
       l1=[]

       for k in range(a[0]*3,a[0]*3+3):
        l1.append(k)

       for k in range(9):

        if(k%3!=b[0] and k not in l1):
         l.append(sud[i][k])

         if(sud[i][k]==0):
          a=k

       if(l.count(0)==1):
        sud[i][a]=j
        row[int(i/3)*3+int(a/3)][3+a%3]=j
        col[3+a%3][int(i/3)*3+int(a/3)]=j
        continue

      elif(len(b)==1 and len(a)==0):

       for k in range(9):

        if(k%3!=b[0]):
         l.append(sud[i][k])

         if(sud[i][k]==0):
          a=k

       if(l.count(0)==1):
        sud[i][a]=j
        row[int(i/3)*3+int(a/3)][3+a%3]=j
        col[3+a%3][int(i/3)*3+int(a/3)]=j
        continue

      elif(len(a)==1 and len(b)==0):

       for k in range(9):

        if(int(k/3)!=a[0]):
         l.append(sud[i][k])

         if(sud[i][k]==0):
          g=k

       if(l.count(0)==1):
        sud[i][g]=j
        row[int(i/3)*3+int(g/3)][3+g%3]=j
        col[3+g%3][int(i/3)*3+int(g/3)]=j
        continue

      else:
       pass

     #i%3==2

     elif(i%3==2):

      if(i==2):
       z=i+3; x=i+6

      elif(i==5):
       z=i-3; x=i+3

      else:
       z=i-6; x=i-3    

      a=[]

      if(sud[i-1].count(j)>0):
       a.append(int(sud[i-1].index(j)/3))

      if(sud[i-2].count(j)>0):
       a.append(int(sud[i-2].index(j)/3))

      b=[]

      if(sud[z].count(j)>0):
       b.append(int(sud[z].index(j)%3))

      if(sud[x].count(j)>0):
       b.append(int(sud[x].index(j)%3))

      if(len(b)==0 and len(a)==0):
       continue

      if(len(a)==2 and len(b)==2):

       for k in range(3):

        if k not in a:
         a=k
         break

       for k in range(3):

        if(k not in b):
         b=k
         break
       sud[i][a*3+b]=j;
       b=a*3+b
       row[int(i/3)*3+int(b/3)][6+b%3]=j
       col[6+b%3][int(i/3)*3+int(b/3)]=j

      elif(len(a)==2 and len(b)!=2):

       for k in range(3):

        if k not in a:
         c=k
         break

       if(sud[i][c*3:c*3+3].count(0)==1):
        a=sud[i][c*3:c*3+3].index(0)
        sud[i][c*3+a]=j
        a=c*3+a
        row[int(i/3)*3+int(a/3)][6+a%3]=j
        col[6+a%3][int(i/3)*3+int(a/3)]=j
        continue

       elif(sud[i][c*3:c*3+3].count(0)==2 and len(b)==1):
        a=sud[i][c*3:c*3+3];

        if(a[b[0]]==0):

         for k in range(3):

          if k not in b:

           if a[k]==0:
            a=k
            break
         sud[i][c*3+a]=j
         a=c*3+a
         row[int(i/3)*3+int(a/3)][6+a%3]=j
         col[6+a%3][int(i/3)*3+int(a/3)]=j
         continue

      elif(len(b)==2 and len(a)!=2):

       for k in range(3):

        if k not in b:
         c=k
         break

       if(col[(i*3+c)%9][int(i/3)*3:int(i/3)*3+3].count(0)==1):
        a=col[(i*3+c)%9][int(i/3)*3:int(i/3)*3+3].index(0)
        q=(i*3+c)%9;
        a=int(i/3)*3+a
        col[q][a]=j
        row[a][q]=j
        sud[int(q/3)+int(a/3)*3][(q%3)+(a%3)*3]=j
        continue

       elif(col[(i*3+c)%9][int(i/3)*3:int(i/3)*3+3].count(0)==2 and len(a)==1):
        b=col[(i*3+c)%9][int(i/3)*3:int(i/3)*3+3];

        if(b[a[0]]==0):

         for k in range(3):

          if k not in a:

           if b[k]==0:
            b=k
            break
         q=(i*3+c)%9
         b=int(i/3)*3+b
         col[q][b]=j
         row[b][q]=j
         sud[int(q/3)+int(b/3)*3][(q%3)+(b%3)*3]=j
         continue

      elif(len(a)==1 and len(b)==1):
       l1=[]

       for k in range(a[0]*3,a[0]*3+3):
        l1.append(k)

       for k in range(9):

        if(k%3!=b[0] and k not in l1):
         l.append(sud[i][k])

         if(sud[i][k]==0):
          g=k

       if(l.count(0)==1):
        sud[i][g]=j
        row[int(i/3)*3+int(g/3)][6+g%3]=j
        col[6+g%3][int(i/3)*3+int(g/3)]=j
        continue

      elif(len(b)==1 and len(a)==0):

       for k in range(9):

        if(k%3!=b[0]):
         l.append(sud[i][k])

         if(sud[i][k]==0):
          a=k

       if(l.count(0)==1):
        sud[i][a]=j
        row[int(i/3)*3+int(a/3)][6+a%3]=j
        col[6+a%3][int(i/3)*3+int(a/3)]=j
        continue

      elif(len(a)==1 and len(b)==0):

       for k in range(9):

        if(int(k/3)!=a[0]):
         l.append(sud[i][k])

         if(sud[i][k]==0):
          g=k

       if(l.count(0)==1):
        sud[i][g]=j
        row[int(i/3)*3+int(g/3)][6+g%3]=j
        col[6+g%3][int(i/3)*3+int(g/3)]=j
        continue

      else:
       pass
 
  if(w==p):
   p=0
 
  else:
   w=p

 def guess(row,r,c,n):
  for x in range(9):
   if row[r][x]==n:
    return False
  for x in range(9):
   if row[x][c]==n:
    return False
  r=r-r%3
  c=c-c%3
  for i in range(3):
   for j in range(3):
    if row[i+r][j+c]==n:
     return False
  return True

 def testandsolve(row,r,c):
  if (r==8 and c==9):
   return True
  if c==9:
   r+=1
   c=0
  if row[r][c]>0:
   return testandsolve(row,r,c+1)
  for n in range(1,10,1):
   if guess(row,r,c,n):
    row[r][c]=n
    if testandsolve(row,r,c+1):
     return True
   row[r][c]=0
  return False
 
 if(testandsolve(row, 0, 0)): 
  flag=1
  return JsonResponse({'row':row,'flag':flag})
 else:
  flag=2
  return JsonResponse({'row':row,'flag':flag})
# Create your views here.
